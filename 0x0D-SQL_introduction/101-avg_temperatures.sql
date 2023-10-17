-- Task: Import table dump into hbtn_0c_0 database and display average temperature by city
-- SQL Query: Import table dump into hbtn_0c_0 database
-- SQL Query: Display average temperature by city ordered by temperature (descending)

SELECT city, AVG(temperature) AS avg_temperature FROM temperature_data GROUP BY city ORDER BY avg_temperature DESC;
