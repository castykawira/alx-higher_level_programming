-- Database name provided as the first command-line argument
-- SQL script to import the database dump
-- SQL script to list shows without a linked genre
-- Use the specified database
-- List shows without a linked genre

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
