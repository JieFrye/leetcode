# A robot is located at the top-left corner of a m x n grid.
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid.
#
# Now consider if some obstacles are added to the grids.
# How many unique paths would there be?

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        '''
        Ideas: at each cell ij, it was reached form (i-1)j or i(j-1).
        If obstacleGrid[i][j] = 1, dp[i][j] = 0
        obstacleGrid = [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
        dp = [
          [1,1,1],
          [1,0,1],
          [1,1,2]
        ]
        '''
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp = [ [0 for j in range(n)] for i in range(m)]
        # first row
        for j in range(n):
            if  obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        # first column
        for i in range(m):
            if  obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        # fill ij-cell
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
sol = Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid))
