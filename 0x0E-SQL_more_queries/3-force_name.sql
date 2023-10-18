-- Check if the database name is provided as an argument
-- Database name provided as the first command-line argument
-- SQL script to create the force_name table

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
