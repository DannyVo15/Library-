[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/pTVdABVF)
# Introduction

The goal of this assignment is to have you create and query a database system of flowers. You are asked to submit a file named **flowers.sql** containing all the necessary SQL commands to create a database with the same name and a few tables according to a predefined schema, populate those tables with some initial data, and query your database. Because this is a small database, you will be using **INSERT INTO** SQL syntax to populate your tables. 

Your **flowers.sql** file MUST have a comment section in the beginning with the name(s) of the author(s) of the project. Use the provided template! You are allowed to work together with another classmate.  You will have points deducted if you fail to properly identify the names of all of the participants of the project. 

# Zones

A flower vendor wants to market flowers that can be grown in a variety of zones. These zones define a range for the lowest (or highest) temperatures that the plants can accept during the year. See map below that illustrates the plant zones in the U.S. according to the United States Department of Agriculture (USDA). 

![pic1.jpeg](pics/pic1.jpeg)

Create a table named **Zones** with the attributes and assumptions indicated below.

* Attributes: the zone ID, the lowest and the highest accepted temperature.
* Assumptions: the ID will be the primary key and have one or two digits, the temperatures (in Fahrenheit) will be at most two digits and a possible minus sign, none of the temperatures can be NULL. 

Populate table **Zones** with the following rows:

```
+----+-----------+------------+
| id | lowerTemp | higherTemp |
+----+-----------+------------+
|  2 |       -50 |        -40 |
|  3 |       -40 |        -30 |
|  4 |       -30 |        -20 |
|  5 |       -20 |        -10 |
|  6 |       -10 |          0 |
|  7 |         0 |         10 |
|  8 |        10 |         20 |
|  9 |        20 |         30 |
| 10 |        30 |         40 |
+----+-----------+------------+
```

# Deliveries

The same flower vendor wants to use a code to explain the type of delivery for each flower. Create a table named **Deliveries** with the attributes and assumptions indicated below. 

* Attributes: the delivery ID, the category or type of delivery, and the size of the delivery. 
* Assumptions: the ID will be the primary key and have one one digit, the category will be at most five characters (pot, plant, hedge, shrub, tree), and the delivery size will be up to five digits with three decimal spaces (possibly NULL). 

Populate table **Deliveries** with the following rows:

```
+----+-------+---------+
| id | categ | delSize |
+----+-------+---------+
|  1 | pot   |   1.500 |
|  2 | pot   |   2.250 |
|  3 | pot   |   2.625 |
|  4 | pot   |   4.250 |
|  5 | plant |    NULL |
|  6 | bulb  |    NULL |
|  7 | hedge |  18.000 |
|  8 | shrub |  24.000 |
|  9 | tree  |  36.000 |
+----+-------+---------+
```

# FlowersInfo

Create a table named **FlowersInfo** with the attributes and assumptions indicated below. Choose the most appropriate data types. 

* Attributes: an ID with three digits, common name, Latin name, the coolest and hottest zones where it can be grown, the delivery category, and the sun needs. 
* Assumptions: The ID will be the primary key, the attribute common name may have up to thirty characters, and the Latin name up to thirty-five characters. The attributes coolest zone, hottest zone, and delivery category will match the IDs from other tables, and the sun needs will be up to five characters, S for Sun, SH for Shade, P for Partial sun and any combination (StoP, StoSH, etc.). Your table definition should implement referential integrity whenever possible. 

Populate table **FlowersInfo** so that it has the following rows:

```
+-----+------------------------+--------------------------------+-------+-------+---------+----------+
| id  | comName                | latName                        | cZone | hZone | deliver | sunNeeds |
+-----+------------------------+--------------------------------+-------+-------+---------+----------+
| 101 | Lady Fern              | Atbyrium filix-femina          |     2 |     9 |       5 | SH       |
| 102 | Pink Caladiums         | C.x bortulanum                 |    10 |    10 |       6 | PtoSH    |
| 103 | Lily-of-the-Valley     | Convallaria majalis            |     2 |     8 |       5 | PtoSH    |
| 105 | Purple Liatris         | Liatris spicata                |     3 |     9 |       6 | StoP     |
| 106 | Black Eyed Susan       | Rudbeckia fulgida var. specios |     4 |    10 |       2 | StoP     |
| 107 | Nikko Blue Hydrangea   | Hydrangea macrophylla          |     5 |     9 |       4 | StoSH    |
| 108 | Variegated Weigela     | W. florida Variegata           |     4 |     9 |       8 | StoP     |
| 110 | Lombardy Poplar        | Populus nigra Italica          |     3 |     9 |       9 | S        |
| 111 | Purple Leaf Plum Hedge | Prunus x cistena               |     2 |     8 |       7 | S        |
| 114 | Thorndale Ivy          | Hedera belix Thorndale         |     3 |     9 |       1 | StoSH    |
+-----+------------------------+--------------------------------+-------+-------+---------+----------+
```

# Queries

Write SQL statements to answer the following queries. Write a comment header right before each SQL statement with the letter of the query answered by the statement. 

a) the total number of zones. 

b) the number of flowers per cool zone. 

c) common names of the plants that have delivery sizes less than 5. 

d) common names of the plants that require full sun (i.e., sun needs contains ‘S’). 

e) all delivery category names order alphabetically (without repetition). 

f) the exact output (note that it is order by Name):

![pic2.png](pics/pic2.png)

g) plant names that have the same hot zone as “Pink Caladiums” (your solution MUST get the hot zone of “Pink Caladiums” in a variable). 

h) the total number of plants, the minimum delivery size, the maximum delivery size, and the average size based on the plants that have delivery sizes (note that the average value should be rounded using two decimals). 

![pic3.png](pics/pic3.png)

i) the Latin name of the plant that has the word ‘Eyed’ in its name (you must use LIKE in this query to get full credit). 

j) the exact output (ordered by Category and then by Name):

![pic4.png](pics/pic4.png)

# Rubric 

```
+5	database, tables, and SQL file have the names suggested, comments were added on the SQL file, including the name of the student(s)
+5	table Zones creation
+5	table Zones population
+5	table Deliveries creation
+5	table Deliveries population
+10	table FlowersInfo creation
+5	table FlowersInfo population 
+25	queries a, b, d, e, and i, +5 each 
+35	+7 for the other queries
-5 failed to identify the names of the project's participants
```
