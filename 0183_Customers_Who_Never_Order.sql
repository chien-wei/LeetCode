# Write your MySQL query statement below
SELECT c.Name AS Customers
FROM Customers c
LEFT JOIN Orders o
On c.Id = o.CustomerId
WHERE o.CustomerId is null;

# Create Test Table
Create table Customers (
    Id INT,
    Name VARCHAR(50)
);
Create table Orders (
    Id INT,
    CustomerId INT
);
Insert into Customers (Id, Name) Values (1, 'Joe'), (2, 'Henry'), (3, 'Sam'), (4, 'Max');
Insert into Orders (Id, CustomerId) Values (1, 3), (2, 1);