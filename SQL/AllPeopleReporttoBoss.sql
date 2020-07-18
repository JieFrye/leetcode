BEGIN TRANSACTION;

/* Create a table*/
CREATE TABLE Employees(employee_id integer PRIMARY KEY,
                       employee_name text,
                       manager_id integer);
INSERT INTO Employees VALUES(1, 'Boss',1);
INSERT INTO Employees VALUES(3,'Alice',3);
INSERT INTO Employees VALUES(2,'Bob',1);
INSERT INTO Employees VALUES(4,'Daniel',2);
INSERT INTO Employees VALUES(7,'Luis',4);
INSERT INTO Employees VALUES(8,'Jhon',3);
INSERT INTO Employees VALUES(9,'Angela',8);
INSERT INTO Employees VALUES(77,'Robert',1);
COMMIT;

/* Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company.
The indirect relation between managers will not exceed 3 managers as the company is small.
The head of the company is the employee with employee_id 1.*/
-- use subquery
SELECT employee_id
FROM Employees
WHERE employee_id <> 1 AND manager_id IN (SELECT employee_id
FROM Employees
WHERE manager_id IN (SELECT employee_id
FROM Employees
WHERE manager_id = 1));

-- use join
SELECT t1.employee_id
FROM Employees AS t1 INNER JOIN Employees AS t2
ON t1.manager_id = t2.employee_id
JOIN Employees AS t3
ON t2.manager_id = t3.employee_id
WHERE t3.manager_id = 1 and t1.employee_id != 1;

-- use recursive cte
Declare @id int;
Set @id = 1;

WITH EmployeeCTE AS
(
  -- Anchor
  SELECT employee_id
  FROM Employees
  WHERE manager_id = @id

  UNION ALL

  -- Recursive Member

  SELECT Employees.employee_id
  FROM Employees JOIN EmployeeCTE
  ON Employees.manager_id = EmployeeCTE.employee_id
)
SELECT * FROM EmployeeCTE
