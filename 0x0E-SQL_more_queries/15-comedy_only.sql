-- Database name provided as the first command-line argument
-- SQL script to import the database dump
-- SQL script to list Comedy shows
-- Use the specified database
-- List Comedy shows

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
