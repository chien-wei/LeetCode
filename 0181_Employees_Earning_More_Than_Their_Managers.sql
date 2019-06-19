# Write your MySQL query statement below
SELECT a.Name AS Employee
FROM Employee a JOIN Employee b
ON a.ManagerID = b.Id
WHERE a.Salary > b.Salary

# Create Test Table
CREATE TABLE IF NOT EXISTS Employee (
    Id INT,
    Name VARCHAR(50),
    Salary INT,
    ManagerId INT
);

DELETE FROM Employee;

INSERT INTO Employee VALUES
(1, 'Joe', 70000, 3),
(2, 'Henry', 80000, 4),
(3, 'Sam', 60000, NULL),
(4, 'Max', 90000, NULL);