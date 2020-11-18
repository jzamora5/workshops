-- GRANT PERMISSIONS
-- GRANT ALL PRIVILEGES ON `relationships`.* TO 'test_user' @'localhost';
-- Create Database
DROP DATABASE IF EXISTS relationships;
CREATE DATABASE IF NOT EXISTS relationships;
USE relationships;
-- ===============================================
-- ONE TO MANY Relationship
CREATE TABLE customers (
  customer_id INT,
  name VARCHAR(128),
  PRIMARY KEY (customer_id)
);
-- ===
CREATE TABLE orders (
  order_id INT,
  customer_id INT,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
-- Insert Data
-- customers
INSERT INTO
  customers (customer_id, name)
VALUES
  (1, 'Tang'),
  (2, 'Larry'),
  (3, 'Peter'),
  (4, 'Mary'),
  (5, 'Tony'),
  (6, 'Steve');
-- orders
INSERT INTO
  orders (order_id, customer_id)
VALUES
  (1, 1),
  (2, 1),
  (3, 1),
  (4, 6),
  (5, 6),
  (6, 6);
SELECT
  *
FROM
  customers;
SELECT
  *
FROM
  orders;
--  JOIN Query ================
SELECT
  *
FROM
  customers as C
  JOIN orders AS O ON C.customer_id = O.customer_id;
--  JOIN Query No Repeat ================
SELECT
  C.*,
  O.order_id
FROM
  customers as C
  JOIN orders AS O ON C.customer_id = O.customer_id;
-- ==