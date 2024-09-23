"""
CS3810: Principles of Database Systems
Instructor: Thyago Mota
Student(s): 
Description: A data load script for the P2 database
"""

import psycopg2
import configparser as cp
import csv

def parse_address(address): 
    try: 
        address, city, state_zipcode = address.split(',')
        city = city.strip()
        state = state_zipcode[:2].strip()
        zipcode = state_zipcode[3:].strip()
        return address, city, state, zipcode
    except: 
        address, complement, city, state_zipcode = address.split(',')
        address = address + ' ' + complement
        address = address.strip()
        city = city.strip()
        state = state_zipcode[:2].strip()
        zipcode = state_zipcode[3:].strip()
        return address, city, state, zipcode

def parse_chemical(chemical):
    try:
        chemical_seq, chemical_name = chemical.split(':')
        chemical_seq = int(chemical_seq)
        chemical_name = chemical_name.strip()
        return chemical_seq, chemical_name
    except: 
        chemical = chemical.replace(':1', ' to 1')
        chemical_seq, chemical_name = chemical.split(':')
        chemical_seq = int(chemical_seq)
        chemical_name = chemical_name.strip()
        return chemical_seq, chemical_name

def parse_industry(industry):
    industry_id, industry_name = industry.split(':')
    industry_id = int(industry_id)
    industry_name = industry_name.strip()
    return industry_id, industry_name

config = cp.RawConfigParser()
config.read('src/config.ini')
params = dict(config.items('db'))
conn = psycopg2.connect(**params)
if conn: 
    print('Connection to Postgres database ' + params['dbname'] + ' was successful!')

    print('Bye!')
    conn.close()