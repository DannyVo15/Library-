-- flowers database
-- created at: July 3rd 2024
-- author(s): Kade Shockey, Danny Vo

-- database creation and use
CREATE DATABASE flowers;
\c flowers
-- tables creation satisfying all of the requirements
CREATE TABLE Zones (
    id INT PRIMARY KEY,
    lowerTemp INT NOT NULL,
    higherTemp INT NOT NULL
);

CREATE TABLE Deliveries (
    id INT PRIMARY KEY,
    category CHAR(5),
    delSize DECIMAL(5, 3)
);

CREATE TABLE FlowersInfo(
    id INT PRIMARY KEY,
    commonName VARCHAR(30),
    latName VARCHAR(35),
    cZone INT,
    hZone INT,
    deliver INT,
    sunNeeds CHAR(5),
    FOREIGN KEY (cZone) REFERENCES Zones(id),
    FOREIGN KEY (hZone) REFERENCES Zones(id),
    FOREIGN KEY (deliver) REFERENCES Deliveries(id)
);
-- tables population
INSERT INTO Zones VALUES 
(2, -50, -40),
(3, -40, -30),
(4, -30, -20),
(5, -20, -10),
(6, -10, 0),
(7, 0, 10),
(8, 10, 20),
(9, 20, 30),
(10, 30, 40);

INSERT INTO Deliveries VALUES
(1, 'pot', 1.500),
(2, 'pot', 2.250),
(3, 'pot', 2.625),
(4, 'pot', 4.250),
(5, 'plant', NULL),
(6, 'bulb', NULL),
(7, 'hedge', 18.000),
(8, 'shrub', 24.000),
(9, 'tree', 36.000);


INSERT INTO FlowersInfo VALUES
('101', 'Lady Fern', 'Atbyrium filix-femina', '2', '9', '5', 'SH'),
('102', 'Pink Caladiums', 'C.x bortulanum', '10', '10', '6', 'PtoSH'),
('103', 'Lily-of-the-Valley', 'Convallaria majalis', '2', '8', '5', 'PtoSH'),
('105', 'Purple Liatris', 'Liatris spicata', '3', '9', '6', 'StoP'),
('106', 'Black Eyed Susan', 'Rudbeckia fulgida var. specios', '4', '10', '2', 'StoP'),
('107', 'Nikko Blue Hydrangea', 'Hydrangea macrophylla', '5', '9', '4', 'StoSH'),
('108', 'Variegated Weigela', 'W. florida Variegata', '4', '9', '8', 'StoP'),
('110', 'Lombardy Poplar', 'Populus nigra Italica', '3', '9', '9', 'S'),
('111', 'Purple Leaf Plum Hedge', 'Prunus x cistena', '2', '8', '7', 'S'),
('114', 'Thorndale Ivy', 'Hedera belix Thorndale', '3', '9', '1', 'StoSH');

-- a) the total number of zones.
SELECT COUNT (*) FROM Zones;
-- b) the number of flowers per cool zone.
SELECT cZone, COUNT(*) as flower_count
FROM FlowersInfo 
GROUP BY cZone; 
-- c) common names of the plants that have delivery sizes less than 5.
SELECT FlowersInfo.commonName
FROM FlowersInfo 
JOIN Deliveries ON FlowersInfo.deliver = Deliveries.id 
WHERE Deliveries.delSize < 5; 
-- d) common names of the plants that require full sun (i.e., sun needs contains ‘S’).
SELECT commonName 
FROM FlowersInfo 
WHERE sunNeeds ~ 'S |Sto.*';
-- e) all delivery category names order alphabetically (without repetition).
SELECT DISTINCT category 
FROM Deliveries 
ORDER BY category;
-- f) the exact output (see instructions)
SELECT commonName, lowerTemp, higherTemp, category
FROM FlowersInfo
INNER JOIN Zones ON FlowersInfo.cZone = Zones.id INNER JOIN Deliveries ON FlowersInfo.deliver = Deliveries.id ORDER BY commonName;
-- g) plant names that have the same hot zone as “Pink Caladiums” (your solution MUST get the hot zone of “Pink Caladiums” in a subQuery).
SELECT commonName
FROM FlowersInfo
WHERE hZone = (
    SELECT hZone
    FROM FlowersInfo
    WHERE commonName = 'Pink Caladiums'
);
-- h) the total number of plants, the minimum delivery size, the maximum delivery size, 
--and the average size based on the plants that have delivery sizes 
--(note that the average value should be rounded using two decimals).

SELECT 
COUNT (FlowersInfo.id) AS totalPlants,
MIN(Deliveries.delSize) AS minDelSize,
MAX(Deliveries.delSize) AS maxDelSize,
ROUND(AVG(Deliveries.delSize),2) AS avgDelSize
FROM FlowersInfo 
JOIN Deliveries ON FlowersInfo.deliver = Deliveries.id;
-- i) the Latin name of the plant that has the word ‘Eyed’ in its name (you must use LIKE in this query to get full credit).  
SELECT latName
FROM FlowersInfo
WHERE commonName LIKE '%Eyed%';
-- j) the exact output (see instructions)
SELECT category, commonName
FROM Deliveries
INNER JOIN FlowersInfo ON Deliveries.id = FlowersInfo.deliver ORDER BY category;