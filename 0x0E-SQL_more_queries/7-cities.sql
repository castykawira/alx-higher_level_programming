-- Database name provided as the first command-line argument
-- SQL script to create the hbtn_0d_usa database and the cities table
-- Create database if not exists
-- Switch to the specified database
-- Create cities table if not exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
