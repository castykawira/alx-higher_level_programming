-- Database name provided as the first command-line argument
-- SQL script to list all cities with corresponding state names
-- Use the specified database
-- List all cities with corresponding state names

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
