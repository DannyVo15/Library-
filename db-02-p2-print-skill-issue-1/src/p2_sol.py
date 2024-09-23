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

    ps1 = '''
        prepare ps1 as 
        INSERT INTO P2 VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12);
    '''

    cur = conn.cursor()
    # cur.execute(ps1) 
    # with open('data/p2.csv', 'rt') as f:
    #     cur = conn.cursor()
    #     drgs = rucas = prvdrs = prvdr_drgs = 0
    #     for row in csv.DictReader(f, delimiter=',', quotechar='"'):
    #         facility_address, facility_city, facility_state, facility_zipcode = parse_address(row['facility_address'])
    #         chemical_seq, chemical_name = parse_chemical(row['chemical'])
    #         industry_id, industry_name = parse_industry(row['industry'])
    #         sql = 'execute ps1 (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    #         cur.execute(sql, (
    #             row['facility_id'], 
    #             row['facility_name'], 
    #             facility_address, 
    #             facility_city, 
    #             facility_state, 
    #             facility_zipcode, 
    #             chemical_seq, 
    #             chemical_name, 
    #             industry_id, 
    #             industry_name, 
    #             int(row['year']), 
    #             round(float(row['amount']), 2)
    #         ))
    #         conn.commit()

    # CHEMICALS 
    print('Inserting into Chemicals...')
    sql = '''
        INSERT INTO Chemicals
            SELECT chemical_seq, chemical_name 
            FROM P2 
            GROUP BY chemical_seq, chemical_name
            ORDER BY chemical_seq
    '''
    cur.execute(sql)
    conn.commit()

    # INDUSTRIES 
    print('Inserting into Industries...')
    sql = '''
        INSERT INTO Industries
            SELECT industry_id, industry_name
            FROM P2 
            GROUP BY industry_id, industry_name
            ORDER BY industry_id
    '''
    cur.execute(sql)
    conn.commit()

    # FACILITIES 
    print('Inserting into Facilities...')
    sql = '''
        INSERT INTO Facilities
            SELECT facility_id, facility_name, facility_address, facility_city, facility_state, facility_zipcode 
            FROM P2 
            GROUP BY facility_id, facility_name, facility_address, facility_city, facility_state, facility_zipcode
            ORDER BY facility_id
    '''
    cur.execute(sql)
    conn.commit()

    # FACILITY_INDUSTRIES
    print('Inserting into Facility_Industries...')
    sql = '''
        INSERT INTO Facility_Industries
            SELECT facility_id, industry_id
            FROM P2 
            GROUP BY facility_id, industry_id
            ORDER BY facility_id, industry_id
    '''
    cur.execute(sql)
    conn.commit()

    # READINGS 
    print('Inserting into Readings...')
    sql = '''
        INSERT INTO Readings
            SELECT facility_id, industry_id, chemical_seq, year, AVG(amount)
            FROM P2 
            GROUP BY facility_id, industry_id, chemical_seq, year
            ORDER BY facility_id, industry_id, chemical_seq, year 
    '''
    cur.execute(sql)
    conn.commit()

    print('Bye!')
    conn.close()