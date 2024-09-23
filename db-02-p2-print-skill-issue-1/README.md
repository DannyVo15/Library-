[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/s5VcnxV6)
# Introduction 

EPA, the national Environmental Protection Agency, collects information to track industry progress in reducing waste generation and moving towards safer waste management alternatives. In this project assignment you are given the p2 (Polution Prevention) dataset in CSV format. Your goal is to create a database from the (unormalized) p2 dataset, which contains information about industrial facilities of different industry groups with the amount of different chemicals released by them per year. 

# Data Model 

The p2 dataset contains 39,249 records with information that span from 2014 to 2022. Below is a summary of each of the attributes of the p2 dataset: 

* facility_id: the TRI (Toxic Release Inventory) facility ID (unique per facility ID);
* facility_name: the name of the facility; 
* facility_address: a compound attribute containing the address of the facility, including its city, state and zipcode; 
* chemical: a compound attribute containing a unique sequence number and the name of a chemical; 
* industry: also a compound attribute containing a unique industry (group) identification and its name; 
* year: the year of the reading; 
* amount: the amount released of the chemical by the facility on that year. 

Note that because there may be multiple readings of the same chemical in a year for the same combination of facility and industry group, you should save in the database the average of all the readings done in a year (for the same chemical and in relation to the same facility and industry group). For example: 

```
02151GLBLP140LE	GLOBAL COMPANIES LLC	117:Ethylbenzene	424710: Petroleum Bulk Stations and Terminals	2013	91.01
02151GLBLP140LE	GLOBAL COMPANIES LLC	117:Ethylbenzene	424710: Petroleum Bulk Stations and Terminals	2013	45.2
02151GLBLP140LE	GLOBAL COMPANIES LLC	117:Ethylbenzene	424710: Petroleum Bulk Stations and Terminals	2013	40.94
```

The facility above (GLOBAL COMPANIES LLC) is of the same industry group (Petroleum Bulk Stations and Terminals) and it has 3 different readings for the same chemical in the same year (2013): 91.01, 45.2, and 40.94. Therefore, you should store in the database the average of the 3 readings, which is 59.05. 

Stats about the dataset: 

* number of facilities: 7,278
* number of industries: 419
* number of distinct chemicals: 327
* number of readings (after averaging multiple reads): 39,136

The goal of this assignment is for you to normalize the given dataset into a Postgres database called **p2**. The **p2** database has to be designed so that all of its tables are normalized up to 3NF (third normal form). All Data Definition Language (DDL) SQL statements (CREATE DATABASE and CREATE TABLE statements) and DCL (Data Control Language) statements (CREATE USER, GRANT statements) should be submitted in a file named **p2.sql**.  In summary, all of the tables of your database should be normalized up to 3NF, have primary keys, and appropriate foreign keys with referential integrity constraints in place. 

You should also create a user named **p2** with full control of all tables in the **p2** database.  Note that any compound attribute should be broken down as that is considered a violation of the first normal form. 

To facilitate grading, the attributes used in your **p2** database MUST preserve the column names of the **p2** dataset (unless it is a renaming of a foreign key). 

# Data Load Script

In order to load the **p2** dataset into your (normalized) **p2** database you are asked to write a data load script in Python. This program should be named **p2.py** and it is the second deliverable of this assignment. Data access secrets (user and password) should be protected in the code using a **config.ini** file. You are required to use the **psycopg2** module to connect and modify the database. 

Please note that you are not allowed to pre-process or modify the CSV file using an external program, like a spreadsheet application, for example.  To be clear: I will test your data load program using the given **p2** dataset. 

# Queries 
 
Your final task in this project is to answer the following queries using SQL. Write your answers to all queries updating the **p2.sql** file.  

a) an alphabetical list of all industries

b) an alphabetical list of all facilities in Colorado 

c) the name of the facility located in Lakewood, Colorado, with its industry name(s)

d) the chemical reading in 2017 from the facility found in query "c" (must include the name of the chemical)

e) the average reading rounded to 2 decimals of the chemical found in query "d" (138: Ethylene oxide) including all of the readings in the database 

f) the number of facilities per state in alphabetical order of the states

g) the names of the facilities that are associated with more than 10 industry groups

h) the industry groups associated with facility named "SHERWIN-WILLIAMS CO" 

i) The average readings (rounded by 2 decimals) per year of the chemical "138:Ethylene oxide" (a cancer-causing substance) in chronological order

j) The name of the chemical that had the highest amount read 

# Grading 

```
+25 Normalization (+5 per table as the normalization process should result in 5 tables)
+10 Tables creation
+5 User creation and grants
+35 Data load script
+25 Queries (+2.5 per query)
-5 didn't write your names in the comments sections of sql and python script
-5 didn't user config.ini for password security 
```