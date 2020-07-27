/* Create a table*/
CREATE TABLE insurance(pid integer PRIMARY KEY, tiv_2011 integer, tiv_2012 integer, lat integer, lon integer);
-- INSERT INTO insurance VALUES(1,100, 1338076, 30,82);
-- INSERT INTO insurance VALUES(2,200,1987,31,82);
-- INSERT INTO insurance VALUES(3,300,295022,31,82);
-- INSERT INTO insurance VALUES(4,100,369024,31,83);
-- INSERT INTO insurance VALUES(5,200,4657,32,82);
INSERT INTO insurance VALUES(1,100,1, 30,82);
INSERT INTO insurance VALUES(2,200,20,31,82);
INSERT INTO insurance VALUES(3,300,300,31,82);
INSERT INTO insurance VALUES(4,100,4000,31,83);
INSERT INTO insurance VALUES(5,200,50000,32,82);
INSERT INTO insurance VALUES(6,200,600000,32,81);

/* sum 2012 tiv over holders who have same 2011 tiv as another holder and (lat, lon) is unique. ans = 1711757 */
SELECT ROUND(SUM(tiv_2012),2)
FROM insurance
WHERE pid IN (SELECT DISTINCT h1.pid
FROM insurance h1, insurance h2
WHERE h1.tiv_2011 = h2.tiv_2011 AND h1.pid <> h2.pid
AND h1.pid NOT IN (SELECT h1.pid
FROM insurance h1, insurance h2
WHERE h1.lat = h2.lat AND h1.lon = h2.lon AND h1.pid <> h2.pid))
