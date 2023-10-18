-- Database name provided as the first command-line argument
-- SQL script to import the database dump
-- SQL script to list genres of the show Dexter
-- Use the specified database
-- List genres of the show Dexter

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
