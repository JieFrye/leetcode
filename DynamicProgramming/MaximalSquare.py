# PD
# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix) -> int:
        # dynamic programming
        '''
        Given a m*n matrix of str, find the largest square containing only 1's
        return its area.
        idea:
        check the three corners of the ij-th entry to update the possible square
        '''
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        mat = [ [0]*(n+1) for i in range(m+1) ]
        maxsq = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    mat[i][j] = 1 + min(mat[i][j-1], mat[i-1][j], mat[i-1][j-1])
                    maxsq = max(maxsq, mat[i][j])
        print(mat)
        print(sum([sum(row) for row in mat]))
        return maxsq**2

matrix = [
['0','1','1','1'],
['1','1','1','1'],
['0','1','1','1']]
sol = Solution()
print(sol.maximalSquare(matrix))
