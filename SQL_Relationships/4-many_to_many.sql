-- GRANT PERMISSIONS
-- GRANT ALL PRIVILEGES ON `relationships`.* TO 'test_user' @'localhost';
-- Create Database
DROP DATABASE IF EXISTS relationships;
CREATE DATABASE IF NOT EXISTS relationships;
USE relationships;
-- ===============================================
-- SELF JOINING Relationship (Unary / Recursive Relationship)
CREATE TABLE students (
  student_id INT,
  first_name VARCHAR(128),
  last_name VARCHAR(128),
  PRIMARY KEY (student_id)
);
-- ===
CREATE TABLE classes (
  class_id INT,
  title VARCHAR(128),
  class_desc VARCHAR(128),
  PRIMARY KEY (class_id)
);
-- == Junction TABLE
CREATE TABLE students_classes (
  sc_id INT,
  student_id INT,
  class_id INT,
  PRIMARY KEY (sc_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (class_id) REFERENCES classes(class_id)
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
-- classes
INSERT INTO
  classes (class_id, title, class_desc)
VALUES
  (1, 'Math', 'Learn the beauty of numbers'),
  (2, 'Physics', 'Discover how the world works'),
  (3, 'Chemistry', 'Learn to master the elements'),
  (4, 'Philosophy', 'What is the meaning of life?'),
  (5, 'English', 'Reinforce your language');
-- students_classes
INSERT INTO
  students_classes (sc_id, student_id, class_id)
VALUES
  (1, 1, 1),
  (2, 1, 3),
  (3, 1, 5),
  (4, 2, 2),
  (5, 2, 4),
  (6, 3, 1),
  (7, 3, 2),
  (8, 3, 3),
  (9, 3, 4),
  (10, 3, 5),
  (11, 4, 2),
  (12, 5, 2),
  (13, 5, 3),
  (14, 5, 4),
  (15, 6, 5),
  (16, 6, 1);
-- ==
SELECT
  *
FROM
  students;
SELECT
  *
FROM
  classes;
SELECT
  *
FROM
  students_classes;
--  JOIN Query ================
SELECT
  S.first_name,
  S.last_name,
  C.title,
  C.class_desc
FROM
  students AS S
  JOIN students_classes AS SC ON S.student_id = SC.student_id
  JOIN classes AS C ON SC.class_id = C.class_id
ORDER BY
  S.first_name;
-- ==