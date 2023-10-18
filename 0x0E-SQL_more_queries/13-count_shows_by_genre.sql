-- Database name provided as the first command-line argument
-- SQL script to import the database dump
-- SQL script to list genres and the number of shows linked to each
-- Use the specified database
-- List genres and the number of shows linked to each

SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
