-- Author: Rusiru Thushara

-- create the database
CREATE DATABASE pet_database;
-- change the database to use
USE pet_database;

-- create the owner table
CREATE TABLE owner (
    owner_id INT NOT NULL,
    surname VARCHAR(60) NOT NULL,
    name VARCHAR(60) NOT NULL,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(50),
    state VARCHAR(50),
    state_full VARCHAR(50),
    zip_code INT,
    PRIMARY KEY (owner_id)
);

-- create the pet table
CREATE TABLE pet (
    pet_id VARCHAR(20) NOT NULL,
    name VARCHAR(60) NOT NULL, 
    kind VARCHAR(60), 
    gender VARCHAR(10), 
    age INT, 
    owner_id INT NOT NULL,
    PRIMARY KEY (pet_id),
    FOREIGN KEY (owner_id) REFERENCES owner(owner_id)
);

-- create the procedure_detail table
CREATE TABLE procedure_detail (
    procedure_type VARCHAR(50) NOT NULL,
    procedure_subcode INT NOT NULL,
    description VARCHAR(255),
    price DECIMAL(15,2),
    PRIMARY KEY (procedure_type, procedure_subcode)
);

-- create the procedure_history table
CREATE TABLE procedure_history (
    pet_id VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    procedure_type VARCHAR(50) NOT NULL,
    procedure_subcode INT NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pet (pet_id),
    FOREIGN KEY (procedure_type, procedure_subcode) REFERENCES procedure_detail (procedure_type,procedure_subcode)
);

-- put the datafiles to the permited directory and use the corresponding path to load

-- load data to the owner table from owner.csv file
LOAD DATA INFILE '/var/lib/mysql-files/dataset/owner.csv' 
INTO TABLE owner 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' 
IGNORE 1 ROWS (owner_id, name, surname, street_address, city, state, state_full, zip_code);

-- load data to the pet table from pet.csv file
LOAD DATA INFILE '/var/lib/mysql-files/dataset/pet.csv'
INTO TABLE pet
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS  (pet_id, name, kind, gender, age, owner_id);

-- load data to the procedure_detail table from procedure_detail.csv
LOAD DATA INFILE '/var/lib/mysql-files/dataset/procedure_detail.csv'
INTO TABLE procedure_detail
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS  (procedure_type, procedure_subcode, description, price);

-- load data to the procedure_history table from procedure_history.csv
LOAD DATA INFILE '/var/lib/mysql-files/dataset/procedure_history.csv'
INTO TABLE procedure_history
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS  (pet_id, date, procedure_type, procedure_subcode);

-- Select all procedure types where the price is above 150
SELECT procedure_type, price 
FROM procedure_detail 
WHERE price > 150;

-- Find all owners who have a parrot as a pet
SELECT owner.name, surname 
FROM owner, pet 
WHERE pet.owner_id = owner.owner_id AND pet.kind = "parrot";

-- Find the number of owners who have the same postal code (i.e 10 from 49503, 1 from 48423)
SELECT owner.zip_code, COUNT(owner.owner_id) AS 'NUMBER OF OWNERS' 
FROM owner GROUP BY owner.zip_code;

-- Find all pets having gone through a procedure during the month of February 2016
SELECT DISTINCT pet.name, pet.pet_id
FROM pet, procedure_history
WHERE pet.pet_id = procedure_history.pet_id
AND EXTRACT(YEAR_MONTH FROM date) = 201602;

-- Find the total cost of procedures incurred during the month of March of owners from the postal code 49503
SELECT SUM(procedure_detail.price)
FROM procedure_detail INNER JOIN procedure_history 
ON procedure_detail.procedure_type = procedure_history.procedure_type
AND procedure_detail.procedure_subcode = procedure_history.procedure_subcode
WHERE procedure_history.pet_id IN 
(
    SELECT pet.pet_id FROM pet, owner  
    WHERE pet.owner_id = owner.owner_id AND owner.zip_code = 49503 
) AND  MONTH(date) = 03;
