DROP USER IF EXISTS 'elearning'@'localhost';
CREATE USER 'elearning'@'localhost' IDENTIFIED BY 'passwd';
GRANT ALL PRIVILEGES ON elearning.* TO 'elearning'@'localhost';
FLUSH PRIVILEGES;
