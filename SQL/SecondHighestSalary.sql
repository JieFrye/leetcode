# Write your MySQL query statement below


/* https://leetcode.com/problems/second-highest-salary/ */
CREATE TABLE Employee(Id integer PRIMARY KEY, Salary integer);

INSERT INTO Employee VALUES(1, 100);
INSERT INTO Employee VALUES(2, 200);
INSERT INTO Employee VALUES(3, 300);
INSERT INTO Employee VALUES(4, 400);
INSERT INTO Employee VALUES(5, 400);

/*
SELECT max(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
*/

SELECT IFNULL(MAX(Salary), NULL) AS SecondHighestSalary
FROM
(SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1 /* skip the highest */
) temp
