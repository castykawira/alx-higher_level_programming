-- Database name provided as the first command-line argument
-- SQL script to create the hbtn_0d_usa database and the states table
-- Create database if not exists
-- Switch to the specified database
-- Create states table if not exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL);
