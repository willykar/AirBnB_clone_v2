<<<<<<< HEAD
-- Prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
=======
-- Prepares a MySQL Test server for the project.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
>>>>>>> e1c784a55e4229df3956360db3d27d6e5e4ab369
