-- GRANT PERMISSIONS
-- GRANT ALL PRIVILEGES ON `relationships`.* TO 'test_user' @'localhost';
-- Create Database
DROP DATABASE IF EXISTS relationships;
CREATE DATABASE IF NOT EXISTS relationships;
USE relationships;
-- ===============================================
-- ONE TO ONE Relationship
CREATE TABLE students (
  student_id INT,
  first_name VARCHAR(128),
  last_name VARCHAR(128),
  PRIMARY KEY (student_id)
);
-- ===
CREATE TABLE contact_info (
  student_id INT UNIQUE NOT NULL,
  city VARCHAR(128),
  phone VARCHAR(128),
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);
-- Insert Data
-- students
INSERT INTO
  students (student_id, first_name, last_name)
VALUES
  (1, 'Tang', 'Sophie'),
  (2, 'Larry', 'Hudson'),
  (3, 'Peter', 'Parker'),
  (4, 'Mary', 'Jane'),
  (5, 'Tony', 'Stark'),
  (6, 'Steve', 'Rogers');
-- contact_info
INSERT INTO
  contact_info (student_id, city, phone)
VALUES
  (6, 'New York', '+3549812'),
  (4, 'San Francisco', '+6745821'),
  (2, 'Chicago', '+98732415');
--
  -- Attempt repeated
  --
  -- INSERT INTO
  -- contact_info (student_id, city, phone)
  -- VALUES
  -- (6, 'New York', '+3549812');
  --
SELECT
  *
FROM
  students;
SELECT
  *
FROM
  contact_info;
--  JOIN Query ================
SELECT
  *
FROM
  students as ST
  JOIN contact_info AS CI ON ST.student_id = CI.student_id;
--  JOIN Query No Repeat ================
SELECT
  ST.*,
  CI.city,
  CI.phone
FROM
  students as ST
  JOIN contact_info AS CI ON ST.student_id = CI.student_id;
-- ==