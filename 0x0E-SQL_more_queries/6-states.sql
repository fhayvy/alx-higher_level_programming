-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- The script won't fail if the database `hbtn_0d_usa` or table `states` already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256)
);
