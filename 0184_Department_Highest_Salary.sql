# Write your MySQL query statement below
SELECT D.Name AS Department, E.Name AS Employee, E.Salary
FROM Department D,
     (SELECT DepartmentId, max(Salary) AS max FROM Employee GROUP BY DepartmentId) T,
     Employee E
WHERE E.DepartmentId = T.DepartmentId
AND E.Salary = T.max
AND D.Id = E.DepartmentId;

# Create Test Table
Create table Employee(
    Id INT,
    Name varchar(20),
    Salary INT,
    DepartmentId INT
);

Insert Into Employee (Id, Name, Salary, DepartmentId) Values
(1, 'Joe', 70000, 1),
(2, 'Henry', 80000, 2),
(3, 'Sam', 60000, 2),
(4, 'Max', 90000, 1);

Create table Department(
    Id INT,
    Name varchar(20)
    );

Insert Into Department (Id, Name) Values
(1, 'IT'),
(2, 'Sales');