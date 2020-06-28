# Given a positive integer n, find the least number of perfect square
# numbers (for example, 1, 4, 9, 16, ...) which sum to n.

class Solution:
    def numSquares(self, n: int) -> int:
        '''
        idea: the subproblems overlap.
        13 - 1 = 12
        13 - 4 = 9
        13 - 9 = 4
        Now we just need to find min # of perfect squares sum to 9, 12, and 4.
        use dp to store all the counts from 0 to n 
        '''
        dp = [0]*(n+1) # at 1, dp[1] = 1 so we need dp[0] = 0
        for x in range(1, n+1):
            min_count = x # using all 1's
            y, sq = 1, 1 # subtract sq 1, 4, 9, 16, ...
            while sq <= x:
                #
                min_count = min(min_count, 1 + dp[x-sq])
                y += 1
                sq = y*y
            dp[x] = min_count
        return dp[n]

sol = Solution()
print(sol.numSquares(4))
