BEGIN TRANSACTION;
/* https://leetcode.com/problems/customers-who-never-order/ */

/* Create a table called Customers */
CREATE TABLE Customers(Id integer PRIMARY KEY, Name text);
/* Create few records in this table */
INSERT INTO Customers VALUES(1,'Joe');
INSERT INTO Customers VALUES(2,'Henry');
INSERT INTO Customers VALUES(3,'Sam');
INSERT INTO Customers VALUES(4,'Max');

CREATE TABLE Orders(Id integer PRIMARY KEY, CustomerId integer);
INSERT INTO Orders VALUES(1, 3);
INSERT INTO Orders VALUES(2, 1);
COMMIT;

/* Display all the records from the table */
SELECT Name AS Customers
FROM Customers LEFT JOIN Orders 
ON Customers.Id = Orders.CustomerId
WHERE Orders.Id IS NULL

