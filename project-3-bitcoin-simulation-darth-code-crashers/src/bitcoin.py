'''
CS 3700 - Networking & Distributed Computing - Fall 2024
Instructor: Thyago Mota
Student(s): Your Name
Description: Project 3 - Bitcoin Mining Simulation
'''

import os
import time
import sys
import stomp
import json
import threading
import hashlib
import random

# TODO: change STUDENT_ID, BROKER_USER, and BROKER_PASSWD
STUDENT_ID = 'dvo7'  # Replace with your student ID
TASKS_TOPIC = f'/queue/bitcoin/{STUDENT_ID}_tasks'
SOLUTIONS_TOPIC = f'/topic/bitcoin/{STUDENT_ID}_solutions'
BROKER_ENDPOINT = '24fcs3700.msudenver.edu'
BROKER_PORT = 61613
BROKER_USER = 'dvo7'
BROKER_PASSWD = '123'

# Semaphore for synchronization
semaphore = threading.Semaphore(1)

# Load tasks from input.txt
def load_tasks(file_name):
    """
    Load tasks from the specified input file.
    Each line in the file represents a task in the format: 'data (bytes), zeros'.
    """
    abs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_name)
    with open(abs_path, 'rt') as f:
        tasks = []
        for line in f:
            line = line.strip()
            data = line.split(',')
            task = {
                'data': [int(value) for value in data[0].split()],
                'zeros': int(data[1])
            }
            tasks.append(task)
        print(f"{len(tasks)} tasks loaded!")
        return list(reversed(tasks))

# Save solution to output.txt
def save_solution(file_name, solution):
    """
    Save the solution to the output file in the same format as input.txt,
    but include the nonce.
    """
    abs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_name)
    with open(abs_path, 'at') as f: 
        for value in solution['data']:
            f.write(f'{value} ')
        f.write(f", {solution['zeros']}, ")
        for value in solution['nonce']:
            f.write(f'{value} ')
        f.write('\n')

# Check if the task is solved
def is_solved(task, digest): 
    """
    Check if the hash digest satisfies the required number of leading zeros.
    """
    for i in range(task['zeros']):
        if digest[i] != 0:
            return False 
    return True

# Mining logic
def mine(conn, id, task):
    """
    Attempt to solve the task by finding a nonce that produces a hash
    with the required number of leading zeros.
    """
    task_solved = threading.Event()  # Local flag for this task
    while not task_solved.is_set():
        nonce = [random.randint(0, 255) for _ in range(32)]
        combined = bytes(task['data']) + bytes(nonce)
        digest = hashlib.md5(combined).digest()

        if is_solved(task, digest):
            task_solved.set()  # Stop mining this task
            solution = {
                'data': task['data'],
                'zeros': task['zeros'],
                'nonce': nonce
            }
            conn.send(body=json.dumps(solution), destination=SOLUTIONS_TOPIC)
            print(f"--> Miner {id} found solution: {solution}")
            save_solution('data/output.txt', solution)

# Tasks listener
class TasksListener(stomp.ConnectionListener):
    def __init__(self, conn, id):
        super().__init__()
        self.conn = conn
        self.id = id

    def on_message(self, frame):
        self.conn.ack(frame.headers['message-id'], frame.headers['subscription'])
        task = json.loads(frame.body)
        print(f"Task received by Miner {self.id}: {task}")
        threading.Thread(target=mine, args=(self.conn, self.id, task)).start()

# Solutions listener
class SolutionsListener(stomp.ConnectionListener):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def on_message(self, frame):
        self.conn.ack(frame.headers['message-id'], frame.headers['subscription'])
        solution = json.loads(frame.body)
        print(f"<-- Solution received: {solution}")

if __name__ == "__main__":
    # Validate parameters
    if len(sys.argv) not in [2, 3]:
        print("Usage: python bitcoin.py m|b [miner_id]")
        sys.exit(1)

    role = sys.argv[1].lower()
    if role not in ['m', 'b']:
        print("Invalid role! Use 'm' for main or 'b' for miner.")
        sys.exit(1)

    print(f"Role is {'main' if role == 'm' else 'bitcoin miner'}")
    id = "main" if role == 'm' else f"miner #{sys.argv[2]}"

    # Set up connections to message broker
    conn_tasks = stomp.Connection([(BROKER_ENDPOINT, BROKER_PORT)])
    conn_solutions = stomp.Connection([(BROKER_ENDPOINT, BROKER_PORT)])
    print("[INFO] Connecting to message broker...")
    conn_tasks.connect(BROKER_USER, BROKER_PASSWD, wait=True)
    conn_solutions.connect(BROKER_USER, BROKER_PASSWD, wait=True)
    print("[INFO] Connected!")

    # Set up listeners based on role
    if role == 'm':
        tasks = load_tasks('data/input.txt')
        for task in tasks:
            conn_tasks.send(body=json.dumps(task), destination=TASKS_TOPIC)
            print(f"[INFO] Published task: {task}")
    elif role == 'b':
        task_listener = TasksListener(conn_tasks, id)
        conn_tasks.set_listener('tasks_listener', task_listener)
        conn_tasks.subscribe(destination=TASKS_TOPIC, id=1, ack='client-individual')

        solution_listener = SolutionsListener(conn_solutions)
        conn_solutions.set_listener('solutions_listener', solution_listener)
        conn_solutions.subscribe(destination=SOLUTIONS_TOPIC, id=2, ack='client-individual')

    # Loop forever to avoid the main thread to end
    while True:
        time.sleep(1)