-- Database name provided as the first command-line argument
-- SQL script to list all cities of California
-- Use the specified database
-- List all cities of California

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
