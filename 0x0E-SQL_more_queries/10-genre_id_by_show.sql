-- Database name provided as the first command-line argument
-- SQL script to import the database dump
-- SQL script to list shows with at least one linked genre
-- Use the specified database
-- List shows with at least one linked genre

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
