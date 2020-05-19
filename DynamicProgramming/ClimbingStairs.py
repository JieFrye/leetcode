# Insight Dynamic Programming
# https://leetcode.com/problems/climbing-stairs/
n = 5

class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        '''
        f(1) = 1 way
        f(2) = 2 ways -> 2 = 1+1 or 2
        f(3) = f(1) + f(2) = 3 -> 3 = 1+2 or 2+1
        f(4) = f(2) + f(3) = 5 -> 4 = 3+1 or 2+2
        f(5) = f(3) + f(4) = 8 -> 5 = 4+1 or 3+2
        Top down + memorization (dictionary)
        '''
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

        #if n == 1:
        #    return 1
        #if n == 2:
        #    return 2
        #return self.climbStairs(n-1) + self.climbStairs(n-2)


sol = Solution()
print(sol.climbStairs(n))
