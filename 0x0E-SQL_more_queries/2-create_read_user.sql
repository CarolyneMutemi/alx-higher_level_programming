-- Creates the database hbtn_0d_2 and the user user_0d_2.

-- Creating Database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creating User.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'User_0d_2_pwd.';
-- Granting permission.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';