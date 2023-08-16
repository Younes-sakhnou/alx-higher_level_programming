-- Defines the 'id_not_null' table with an 'id' column (INT, DEFAULT 1) and a 'name' column (VARCHAR)
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id`   INT          DEFAULT 1,
    `name` VARCHAR(256)
);
