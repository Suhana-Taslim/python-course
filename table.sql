-- 1. Create the table
CREATE TABLE Employees (
    EmpID    INT PRIMARY KEY,
    Name     VARCHAR(50),
    Country  VARCHAR(50),
    Age      INT
);

-- 2. Insert sample data
INSERT INTO Employees (EmpID, Name, Country, Age) VALUES
  (1, 'Amit', 'India', 25),
  (2, 'Sita', 'USA', 30),
  (3, 'Rahul', 'India', 18),
  (4, 'Priya', 'Canada', 28);

-- 3. Select all employees
SELECT * FROM Employees;

-- 4. Select employees from India
SELECT * FROM Employees WHERE Country = 'India';

-- 5. Select names of employees older than 25
SELECT Name, Age FROM Employees WHERE Age > 25;

-- 6. Combined filter
SELECT * FROM Employees 
WHERE Country = 'India' AND Age >= 20;
