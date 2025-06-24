CREATE TABLE departments (
  department_id INT PRIMARY KEY,
  department_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  department_id INT,
  salary DECIMAL(10,2),
  FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_id, department_name) VALUES
  (1, 'HR'),
  (2, 'Finance'),
  (3, 'Engineering'),
  (4, 'Sales');

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
  (101, 'Rita', 'Sharma', 1, 50000),
  (102, 'Ajay', 'Kumar', 2, 60000),
  (103, 'Sara', 'Patel', 3, 70000),
  (104, 'Deepa', 'Nair', 2, 65000),
  (105, 'Vijay', 'Reddy', 4, 55000);

SELECT
  e.*,
  agg.total_salary,
  agg.avg_salary,
  agg.dept_count,
  agg.min_salary,
  agg.max_salary
FROM employees AS e
CROSS JOIN (
  SELECT
    SUM(salary) AS total_salary,
    AVG(salary) AS avg_salary,
    COUNT(DISTINCT department_id) AS dept_count,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
  FROM employees
) AS agg;
