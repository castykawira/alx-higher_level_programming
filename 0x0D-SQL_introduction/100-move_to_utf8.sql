-- Task: Convert hbtn_0c_0 database, first_table table, and name field to UTF8
-- SQL Query: Convert the database to UTF8
-- SQL Query: Convert the table to UTF8
-- SQL Query: Convert the name field to UTF8

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
USE hbtn_0c_0; ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
