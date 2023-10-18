-- Check if the database name is provided as an argument
-- Database name provided as the first command-line argument
-- SQL script to create the unique_id table
-- Create table if not exists

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
