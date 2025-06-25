CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  country VARCHAR(100)
);

CREATE TABLE products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  category VARCHAR(50),
  price DECIMAL(10,2)
);

CREATE TABLE exports (
  export_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT,
  product_id INT,
  export_country VARCHAR(100),
  export_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers (name,email,country) VALUES
('Aaron Orville','aaron@example.com','USA'),
('Alice Morgan','alice@example.com','UK'),
('Bob Smith','bob@example.com','Canada'),
('Adorant Orin','adorant@example.com','India'),
('Arnold','arnold@example.com','Australia');

INSERT INTO products (name,category,price) VALUES
('Orchid Vase','Home Decor',49.99),
('Anchor Bracelet','Accessories',19.99),
('Orbit Drone','Electronics',299.99),
('Organic Soap','Beauty',5.99);

INSERT INTO exports (customer_id,product_id,export_country,export_date) VALUES
(1,3,'Japan','2025-01-15'),
(2,1,'Germany','2025-02-10'),
(4,2,'France','2025-03-05'),
(5,4,'Canada','2025-04-20'),
(1,4,'Mexico','2025-05-25');

SELECT
  c.customer_id,
  c.name,
  c.email,
  c.country AS customer_country,
  p.product_id,
  p.name AS product_name,
  p.category,
  p.price,
  e.export_country,
  e.export_date
FROM customers c
JOIN exports e ON c.customer_id = e.customer_id
JOIN products p ON p.product_id = e.product_id
WHERE c.name LIKE 'A%' 
  AND c.name LIKE '%or%' 
ORDER BY c.customer_id, e.export_date;
