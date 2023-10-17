-- Task: List all records with a name value in the table second_table
-- SQL Query: List records with a name value, ordered by descending score

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
