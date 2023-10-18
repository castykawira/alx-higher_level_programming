-- Database name provided as the first command-line argument
-- SQL script to import the database dump
-- SQL script to list shows with genre IDs
-- Use the specified database
-- List shows with genre IDs

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
