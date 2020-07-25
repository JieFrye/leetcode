/* Create a table*/
CREATE TABLE insurance(pid integer PRIMARY KEY, tiv_2011 integer, tiv_2012 intger, lat integer, lon iteger);
INSERT INTO insurance VALUES(1,100, 1338076, 30,82);
INSERT INTO insurance VALUES(2,200,1987,31,82);
INSERT INTO insurance VALUES(3,300,295022,31,82);
INSERT INTO insurance VALUES(4,100,369024,31,83);
INSERT INTO insurance VALUES(5,200,4657,32,82);


/* sum 2012 tiv over holders who have same 2011 tiv as another holder and (lat, lon) is unique. ans = 1711757 */
SELECT ROUND(SUM(h.tiv_2012),2)
FROM (insurance h1 JOIN insurance h2
ON h1.tiv_2011 = h2.tiv_2011 and h1.pid <> h2.pid) AS h
WHERE h.pid in (SELECT pid
FROM insurance
GROUP BY lat, lon
HAVING count(pid) = 1);
