/*  */

/* Create a table*/
CREATE TABLE Trips(Id integer PRIMARY KEY, Client_Id integer,
                   Driver_Id integer, City_Id integer, Status text,
                   Request_at text);

/* Create few records in this table */
INSERT INTO Trips VALUES(1,1,10,1,'completed', '2013-10-01');
INSERT INTO Trips VALUES(2,2,11,1,'cancelled_by_driver','2013-10-01');
INSERT INTO Trips VALUES(3,3,12,6,'completed', '2013-10-01');
INSERT INTO Trips VALUES(4,4,13,6,'cancelled_by_client','2013-10-01');
INSERT INTO Trips VALUES(5,1,10,1,'completed', '2013-10-02');
INSERT INTO Trips VALUES(6,2,11,6,'completed', '2013-10-02');
INSERT INTO Trips VALUES(7,3,12,6,'completed', '2013-10-02');
INSERT INTO Trips VALUES(8,2,12,12,'completed', '2013-10-03');
INSERT INTO Trips VALUES(9,3,10,12,'completed', '2013-10-03');
INSERT INTO Trips VALUES(10,4,13,12,'cancelled_by_driver','2013-10-03');

/* Create a table*/
CREATE TABLE Users(Users_Id integer PRIMARY KEY, Banned text,
                   Role text);

/* Create few records in this table */
INSERT INTO Users VALUES(1,'No','client');
INSERT INTO Users VALUES(2,'Yes','client');
INSERT INTO Users VALUES(3,'No','client');
INSERT INTO Users VALUES(4,'No','client');
INSERT INTO Users VALUES(10,'No','driver');
INSERT INTO Users VALUES(11,'No','driver');
INSERT INTO Users VALUES(12,'No','driver');
INSERT INTO Users VALUES(13,'No','driver');

/* Display all the records from the table */
SELECT Request_at as Day,
       ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips
WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
      AND Client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
GROUP BY Request_at;
