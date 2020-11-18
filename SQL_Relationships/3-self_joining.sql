-- GRANT PERMISSIONS
-- GRANT ALL PRIVILEGES ON `relationships`.* TO 'test_user' @'localhost';
-- Create Database
DROP DATABASE IF EXISTS relationships;
CREATE DATABASE IF NOT EXISTS relationships;
USE relationships;
-- ===============================================
-- SELF JOINING Relationship (Unary / Recursive Relationship)
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR(128),
  last_name VARCHAR(128),
  manager_id INT DEFAULT NULL,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
-- Insert Data
-- employees
INSERT INTO
  employees (employee_id, first_name, last_name)
VALUES
  (1, 'Tang', 'Sophie'),
  (2, 'Larry', 'Hudson'),
  (3, 'Peter', 'Parker'),
  (4, 'Mary', 'Jane'),
  (5, 'Tony', 'Stark'),
  (6, 'Steve', 'Rogers');
SELECT
  *
FROM
  employees;
-- ADD Manager ID =======
UPDATE
  employees
SET
  manager_id = 6
WHERE
  employee_id IN (1, 2, 3);
-- ==
UPDATE
  employees
SET
  manager_id = 1
WHERE
  employee_id = 4;
-- ==
UPDATE
  employees
SET
  manager_id = 3
WHERE
  employee_id = 5;
-- ==
SELECT
  *
FROM
  employees;
--  JOIN Query ================
  -- ALL Places that answer to Steve
SELECT
  CONCAT(E.first_name, ' ', E.last_name) AS Employee,
  CONCAT(M.first_name, ' ', M.last_name) AS Manager
FROM
  employees as E
  JOIN employees as M ON E.manager_id = M.employee_id;
-- ==