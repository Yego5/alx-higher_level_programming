-- Lists all the cities of California in the database hbtn_0d_usa.
-- The results are ordered by ascending cities.id.
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
-- @shachz  redo
