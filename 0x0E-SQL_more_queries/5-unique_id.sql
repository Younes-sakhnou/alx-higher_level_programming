-- Defines the 'unique_id' table with an 'id' column (INT, DEFAULT 1, UNIQUE constraint) and a 'name' column (VARCHAR)
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
