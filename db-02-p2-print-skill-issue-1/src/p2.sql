-- CS3810: Principles of Database Systems
-- Instructor: Thyago Mota
-- Student(s): 
-- Description: P2 database

DROP DATABASE p2;

CREATE DATABASE p2;

\c p2

-- create tables
CREATE TABLE facilities (
    facilities_id SERIAL PRIMARY KEY,
    facilities_name VARCHAR(100) NOT NULL, 
    facilities_address TEXT NOT NULL.
    chemical VARCHAR(100) NOT NUll, 
    industry VARCHAR(100) NOT NULL.
    year INT NOT NULL, 
    amount NUMERIC(10, 2) NOT NULL
);

-- create user with appropriate access to the tables

-- queries

-- a) an alphabetical list of all industries
    SELECT DISTINCT industries FROM facilities ORDER BY industry;

-- b) an alphabetical list of all facilities in Colorado 
    SELECT facility_name 
    FROM facilities 
    WHERE facility_address LIKE '%Colorado'
    ORDER BY facility_name; 
    
-- c) the name of the facility located in Lakewood, Colorado, with its industry name(s)
    SELECT facility_name, industry FROM facilities WHERE facilities_address LIKE '%Lakewood, Colorado%';
-- d) the chemical reading in 2017 from the facility found in query "c" (must include the name of the chemical)
    SELECT chemical, amount FROM facilities WHERE facility_address LIKE 'Lakewood, Colorado%' AND year = 2017;
-- e) the average reading rounded to 2 decimals of the chemical found in query "d" (138: Ethylene oxide) including all of the readings in the database 

-- f) the number of facilities per state in alphabetical order of the states
    SELECT SUBSTRING(facilities_address FROM '([A-Za-z ]+)$, ') AS state 
    COUNT(*) AS facility_count 
    FROM facilities 
    GROUP BY state 
    ORDER BY state;
-- g) the names of the facilities that are associated with more than 10 industry groups
     SELECT facility_name
     FROM facilities
     GROUP BY facility_name
     HAVING COUNT(DISTINCT industry) > 10;

-- h) the industry groups associated with facility named "SHERWIN-WILLIAMS CO" 
    SELECT DISTINCT industry
    FROM facilities
    WHERE facility_name = 'SHERWIN-WILLIAMS CO';

-- i) The average readings (rounded by 2 decimals) per year of the chemical "138:Ethylene oxide" (a cancer-causing substance) in chronological order
    SELECT year, ROUND(AVG(amount), 2) AS average_reading
    FROM facilities
    WHERE chemical = '138:Ethylene oxide'
    GROUP BY year
    ORDER BY year;

-- j) The name of the chemical that had the highest amount read 
        SELECT chemical, amount
        FROM facilities
        ORDER BY amount DESC
        LIMIT 1;
