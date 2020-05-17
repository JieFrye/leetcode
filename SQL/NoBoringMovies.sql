/* https://leetcode.com/problems/not-boring-movies/ */

CREATE TABLE cinema(id integer PRIMARY KEY, movie text, 
                    description text, rating float);

INSERT INTO cinema VALUES(1, "War", "great 3D", 8.9);
INSERT INTO cinema VALUES(2, "Science", "fiction", 8.5);
INSERT INTO cinema VALUES(3, "irish", "boring", 6.2);
INSERT INTO cinema VALUES(4, "Ice song", "Fantacy", 8.6);
INSERT INTO cinema VALUES(5, "House card", "Interesting", 9.1);

/* Display all the records from the table */
SELECT * 
FROM cinema
WHERE id % 2 = 1 AND description != "boring"
ORDER BY rating DESC;
