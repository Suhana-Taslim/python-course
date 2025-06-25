CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    job_title VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(12,2),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id) ON DELETE SET NULL
);

CREATE TABLE employee_details (
    employee_id INT PRIMARY KEY,
    date_of_birth DATE,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    emergency_contact VARCHAR(100),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);

INSERT INTO employees (first_name, last_name, email, phone, hire_date, job_title, department, salary, manager_id) VALUES
('Harsh', 'Patel', 'harsh.patel@example.com', '+91-9876543210', '2020-07-01', 'CEO', 'Executive', 250000.00, NULL),
('Anjali', 'Kumari', 'anjali.kumari@example.com', '0495-1234567', '2021-03-15', 'HR Manager', 'Human Resources', 120000.00, 1),
('Rahul', 'Sharma', 'rahul.sharma@example.com', '0495-7654321', '2022-01-20', 'Software Engineer', 'Engineering', 90000.00, 1),
('Priya', 'Iyer', 'priya.iyer@example.com', '0495-2345678', '2023-05-10', 'Accountant', 'Finance', 70000.00, 1);

INSERT INTO employee_details (employee_id, date_of_birth, address, city, state, emergency_contact) VALUES
(1, '1980-04-15', '123, MG Road', 'Chennai', 'TN', 'Leela Patel: +91‑9123456789'),
(2, '1990-09-22', '456, Park Street', 'Kolkata', 'WB', 'Sunil Kumar: +91‑9234567890');

SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    e.email,
    e.phone,
    e.hire_date,
    e.job_title,
    e.department,
    e.salary,
    m.first_name AS manager_first_name,
    m.last_name AS manager_last_name,
    d.date_of_birth,
    d.address,
    d.city,
    d.state,
    d.emergency_contact
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
LEFT JOIN employee_details d ON e.employee_id = d.employee_id
ORDER BY e.employee_id;
