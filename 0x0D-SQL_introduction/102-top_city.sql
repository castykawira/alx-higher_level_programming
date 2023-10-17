-- Task: Import table dump into hbtn_0c_0 database and display top 3 cities' temperatures during July and August
-- SQL Query: Import table dump into hbtn_0c_0 database
-- SQL Query: Display top 3 cities' temperatures during July and August ordered by temperature (descending)

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
