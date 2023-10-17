-- Task: List records with a score >= 10 in the table second_table in the specified MySQL database
-- SQL Query: List records with score >= 10 ordered by score

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
