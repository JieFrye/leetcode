/* https://leetcode.com/problems/rank-scores/ */

CREATE TABLE Scores(Id integer PRIMARY KEY, Score float);

INSERT INTO Scores VALUES(1,3.50);
INSERT INTO Scores VALUES(2,3.65);
INSERT INTO Scores VALUES(3,4.00);
INSERT INTO Scores VALUES(4,3.85);
INSERT INTO Scores VALUES(5,4.00);
INSERT INTO Scores VALUES(6,3.65);


/* rank scores allowing tie without gap */
SELECT A.Score AS Score, COUNT(B.Score) AS 'Rank'
FROM Scores A, (SELECT DISTINCT Score FROM Scores) B
WHERE A.Score <= B.Score
GROUP BY A.Id 
ORDER BY A.Score DESC;

