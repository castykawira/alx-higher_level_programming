-- Task: List the number of records with the same score in the table second_table
-- SQL Query: List scores and the number of records, sorted by the number of records

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC, score;
