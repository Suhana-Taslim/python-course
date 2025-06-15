-- Create sample table
CREATE TABLE customer (
  customer_id   INT PRIMARY KEY,
  cust_name     VARCHAR(100),
  city          VARCHAR(50),
  grade         INT,
  salesman_id   INT
);

-- Sample data insertion
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES
 (3002, 'Nick Rimando',  'New York', 100, 5001),
 (3007, 'Brad Davis',    'New York', 200, 5001),
 (3005, 'Graham Zusi',   'California', 200, 5002),
 (3008, 'Julian Green',  'London',    300, 5002),
 (3004, 'Fabian Johnson','Paris',     300, 5006),
 (3009, 'Geoff Cameron', 'Berlin',    100, 5003),
 (3003, 'Jozy Altidor',  'Moscow',    200, 5007);

-- 1. OR condition query
SELECT * FROM customer
WHERE city = 'New York'
   OR grade > 100;

-- 2. AND condition query
SELECT * FROM customer
WHERE city = 'New York'
  AND grade > 100;
