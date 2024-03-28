-- Creates the table unique_id on your MySQL server
-- The script doesn't fail if the table already exits
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
