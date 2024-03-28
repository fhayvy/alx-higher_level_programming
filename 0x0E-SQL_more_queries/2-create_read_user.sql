-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 has only SELECT privilege
-- The script won't fail if the database hbtn_0d_2 or the user user_0d_2 already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'USER_0d_2'@'localhost';
FLUSH PRIVILEGES;
