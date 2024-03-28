-- Creates the table force_name on your MySQL server
-- The script won't fail if the table force_name already exists
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
