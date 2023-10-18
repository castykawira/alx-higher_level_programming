-- Check if the database name is provided as an argument
-- Database name provided as the first command-line argument
-- SQL script to create the id_not_null table

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
