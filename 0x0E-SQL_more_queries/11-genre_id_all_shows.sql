-- Retrieves all shows from 'hbtn_0d_tvshows', displaying NULL for shows without genres, and orders by title and genre ID.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
