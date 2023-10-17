-- Task: Import table dump into hbtn_0c_0 database and display max temperature of each state
-- SQL Query: Import table dump into hbtn_0c_0 database
-- SQL Query: Display max temperature of each state ordered by state name

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
