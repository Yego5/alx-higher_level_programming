-- It lists all genres of the database hbtn_0d_tvshows
-- and not linked to the show Dexter.
-- records are sorted by ascending genre name.
RE tv_genres.id NOT IN (
      SELECT tv_genres.id FROM tv_genres
      JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
      JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
      WHERE tv_shows.title = "DEXTER" )
ORDER BY tv_genres.name;
-- @Shachz.
