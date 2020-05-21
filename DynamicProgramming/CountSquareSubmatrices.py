# Leet Code May 21
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix) -> int:
        '''
        Given a m * n matrix of int ones and zeros, return the numbers of
        square submatrices having all ones.
        idea:
        use a (m+1) * (n+1) matrix to keep track of the squares made at each
        ij-th position
        '''
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        mat = [ [0]*(n+1) for i in range(m+1) ]
        count = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 1:
                    mat[i][j] = 1 + min(mat[i][j-1], mat[i-1][j], mat[i-1][j-1])
                    count += mat[i][j]
        return count

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1] ]

sol = Solution()
print(sol.countSquares(matrix))
