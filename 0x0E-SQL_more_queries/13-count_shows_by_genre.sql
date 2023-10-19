-- The code lists all genres from the database hbtn_0d_tvshows along with the number of
-- Shows linked to each.
-- It does not display genres without linked shows.
-- also records are ordered by descending number of shows linked.
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
-- @shachz. redo
