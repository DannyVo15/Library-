-- CS3810: Principles of Database Systems
-- Instructor: Thyago Mota
-- Student(s): 
-- Description: P2 database

DROP DATABASE p2;

CREATE DATABASE p2;

\c p2

-- create tables

CREATE TABLE P2 (
    facility_id VARCHAR(15), 
    facility_name VARCHAR(150),
    facility_address VARCHAR(150), 
    facility_city VARCHAR(150),
    facility_state CHAR(2), 
    facility_zipcode CHAR(10), 
    chemical_seq INT, 
    chemical_name VARCHAR(150), 
    industry_id INT, 
    industry_name VARCHAR(150), 
    year INT, 
    amount DECIMAL(12, 2)
);

CREATE TABLE Chemicals (
    chemical_seq INT PRIMARY KEY, 
    chemical_name VARCHAR(150)
); 

CREATE TABLE Industries (
    industry_id INT PRIMARY KEY, 
    industry_name VARCHAR(150)
);

CREATE TABLE Facilities (
    facility_id VARCHAR(15) PRIMARY KEY, 
    facility_name VARCHAR(150),
    facility_address VARCHAR(150), 
    facility_city VARCHAR(150),
    facility_state CHAR(2),
    facility_zipcode CHAR(10)
);

CREATE TABLE Facility_Industries (
    facility_id VARCHAR(15),
    industry_id INT, 
    PRIMARY KEY (facility_id, industry_id),
    FOREIGN KEY (facility_id) REFERENCES Facilities (facility_id), 
    FOREIGN KEY (industry_id) REFERENCES Industries (industry_id) 
);

CREATE TABLE Readings (
    facility_id VARCHAR(15), 
    industry_id INT, 
    chemical_seq INT, 
    year INT, 
    PRIMARY KEY (facility_id, industry_id, chemical_seq, year), 
    amount DECIMAL(12, 2), 
    FOREIGN KEY (facility_id) REFERENCES Facilities (facility_id), 
    FOREIGN KEY (industry_id) REFERENCES Industries (industry_id),
    FOREIGN KEY (chemical_seq) REFERENCES Chemicals (chemical_seq)
);

-- create user with appropriate access to the tables

CREATE USER p2 WITH PASSWORD '135791';
GRANT ALL ON TABLE P2 TO "p2";
GRANT ALL ON TABLE Chemicals TO "p2";
GRANT ALL ON TABLE Industries TO "p2";
GRANT ALL ON TABLE Facilities TO "p2";
GRANT ALL ON TABLE Facility_Industries TO "p2";
GRANT ALL ON TABLE Readings TO "p2";


-- queries

-- a) an alphabetical list of all industries
SELECT * FROM Industries ORDER BY industry_name;

-- b) an alphabetical list of all facilities in Colorado 
SELECT * FROM Facilities WHERE facility_state = 'CO' ORDER BY facility_name;

-- c) the name of the facility located in Lakewood, Colorado, with its industry name
SELECT facility_name, industry_name 
FROM Facilities A
INNER JOIN Industries B
ON A.industry_id = B.industry_id 
WHERE facility_city = 'LAKEWOOD' AND facility_state = 'CO';

-- a) an alphabetical list of all industries
SELECT * FROM Industries ORDER BY industry_name;

-- b) an alphabetical list of all facilities in Colorado 
SELECT * FROM Facilities WHERE facility_state = 'CO' ORDER BY facility_name;

--c) the facility located in Lakewood, Colorado, with its industry name(s)
SELECT facility_name, industry_name 
FROM Facilities A 
INNER JOIN Facility_Industries B 
ON A.facility_id = B.facility_id 
INNER JOIN Industries C 
ON B.industry_id = C.industry_id
WHERE facility_state = 'CO' AND facility_city = 'LAKEWOOD';

-- d) the chemical reading in 2017 from the facility found in query "c" (must include the name of the chemical)
SELECT facility_name, industry_name, chemical_name, amount
FROM Facilities A 
INNER JOIN Facility_Industries B 
ON A.facility_id = B.facility_id 
INNER JOIN Industries C 
ON B.industry_id = C.industry_id
INNER JOIN Readings D 
ON A.facility_id = D.facility_id 
INNER JOIN Chemicals E 
ON D.chemical_seq = E.chemical_seq
WHERE facility_state = 'CO' AND facility_city = 'LAKEWOOD' AND year = 2017;

-- e) the average reading rounded to 2 decimals of the chemical found in query "d" (138: Ethylene oxide) including all of the readings in the database 
SELECT ROUND(AVG(amount),2)
FROM Readings 
WHERE chemical_seq = 138;

-- f) the number of facilities per state in alphabetical order of the states
SELECT facility_state, COUNT(*) as total 
FROM Facilities 
GROUP BY facility_state
ORDER BY facility_state;

-- g) the names of the facilities that are associated with more than 10 industry groups
SELECT * FROM (
    SELECT facility_name, COUNT(*) AS total
    FROM Facilities A 
    INNER JOIN Facility_Industries B 
    ON A.facility_id = B.facility_id 
    GROUP BY facility_name
) 
WHERE total > 10
ORDER BY total DESC;

-- h) the industry groups associated with facility named "SHERWIN-WILLIAMS CO" 
SELECT DISTINCT industry_name 
FROM Facilities A 
INNER JOIN Facility_Industries B 
ON A.facility_id = B.facility_id 
INNER JOIN Industries C 
ON B.industry_id = C.industry_id
WHERE facility_name = 'SHERWIN-WILLIAMS CO'
ORDER BY industry_name;

-- i) The average readings (rounded by 2 decimals) per year of the chemical "138:Ethylene oxide" (a cancer-causing substance) in chronological order
SELECT year, ROUND(AVG(amount),2)
FROM Readings 
WHERE chemical_seq = 138
GROUP BY year, chemical_seq 
ORDER BY year;

-- j) The name of the chemical that had the highest amount read 
SELECT chemical_name, amount 
FROM Readings A 
INNER JOIN Chemicals B 
ON A.chemical_seq = B.chemical_seq 
ORDER BY amount DESC
LIMIT 1;