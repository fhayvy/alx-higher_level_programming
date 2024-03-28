-- Creates the table `id_not_null` on your MySQL server
-- The script won't fail if the table `id_not_null` exists
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
