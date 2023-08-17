-- Retrieves all cities in the 'hbtn_0d_usa' database belonging to the state of California (CA).
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
