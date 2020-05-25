# We write the integers of the lists A and B on two separate horizontal lines.
# A straight line connecting two numbers A[i] and B[j] such that:
# 1. A[i] == B[j];
# 2. The line we draw does not intersect any other connecting line.
# Note that a connecting lines cannot intersect even at the endpoints:
# each number can only belong to one connecting line.
#
# Return the maximum number of connecting lines we can draw in this way.

class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        '''
        Define a matrix L to keep track of the connecting lines.
        idea:
            1   4   2  A = [1, 4, 2]
        1   1   1   1  (if B = [1], there is only one line)
        2   1   1   2  (if B = [1, 2], there is two lines)
        4   1   2   2
        ______________ A = [1, 2, 4]
            1   2   4
        1   1   1   1  (if B = [1], there is only one line)
        2   1   2   2  (if B = [1, 2], there is two lines)
        4   1   2   3  if A[i] == B[i], the add 1 to the diag
                     else, max( row above or column left)
        '''
        a = len(A)
        b = len(B)
        L = [[0 for j in range(b+1)] for i in range(a+1)]
        for i in range(a):
            for j in range(b):
                if A[i] == B[j]:
                    L[i+1][j+1] = L[i][j] + 1
                else:
                    L[i+1][j+1] = max(L[i+1][j], L[i][j+1])
        return L[a][b]

# A = [2,2,1,4,4,4]
# B = [4,4,4,1,2,2]
A = [1,3,7,1,7,5]
B = [1,9,2,5,1]
sol = Solution()
print(sol.maxUncrossedLines(A, B))

L = [[0 for j in range(1+1)] for i in range(2+1)]
L[1][1] = 5
print(L)
L = [[0]*2]*3
L[1][1] = 5
print(L)
