# Unique Paths
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid.
#
# How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Ideas: at each cell ij, it was reached form (i-1)j or i(j-1).
        Use bottom-up approach.
        Each cell at the last row and last column has only 1 way to go.

        '''
        paths = [ [1 for j in range(n)] for i in range(m)]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                paths[i][j] = paths[i+1][j] + paths[i][j+1]
        return paths[0][0]


sol = Solution()
print(sol.uniquePaths(7,3))
