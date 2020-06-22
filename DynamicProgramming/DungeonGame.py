# Dungeon Game
# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid
# out in a 2D grid. Our valiant knight (K) was initially positioned in the
# top-left room and must fight his way through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer.
# If at any point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons, so the knight loses health
# (negative integers) upon entering these rooms; other rooms are either
# empty (0's) or contain magic orbs that increase the knight's health
# (positive integers).
#
# In order to reach the princess as quickly as possible, the knight decides
# to move only rightward or downward in each step.
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        '''
        ideas: bottom up
        when a room has positive integer, the min energy required is 1
        before getting there.
        '''
        m, n = len(dungeon), len(dungeon[0])
        dp = [ [0 for j in range(n)] for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # last row and column
                if i == m-1 and j == n-1:
                    dp[i][j] = min(0, dungeon[i][j])
                # last row, can only go to the right
                elif i == m-1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i][j+1])
                # last column, can only go down
                elif j == n-1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i+1][j])
                # to spend min energy in any cell
                else:
                    dp[i][j] = min(0, dungeon[i][j]+max(dp[i+1][j], dp[i][j+1]))
        return abs(dp[0][0])+1

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
sol = Solution()
print(sol.calculateMinimumHP(dungeon))
