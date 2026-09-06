CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL CHECK (age BETWEEN 18 AND 60),
    gender VARCHAR(20) NOT NULL CHECK (gender IN ('Male', 'Female', 'Other')),
    department VARCHAR(50) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) NOT NULL CHECK (salary > 0),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL
);

SELECT * FROM employee_db.employees;