-- Creates the 'hbtn_0d_usa' database and defines the 'cities' table within.
-- The 'cities' table includes an 'id' column (PRIMARY KEY), 'state_id' (FOREIGN KEY referencing 'states' table), and 'name' column.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    PRIMARY KEY(`id`),
    `id`       INT          NOT NULL AUTO_INCREMENT,
    `state_id` INT          NOT NULL,
    `name`     VARCHAR(256) NOT NULL,
    FOREIGN KEY(`state_id`)
    REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
