# Regular Expression Matching
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z,
# and characters like . or *.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Use dp with conditions.
        '''
        m = len(s) + 1
        n = len(p) + 1
        dp = [ [False]*n for i in range(m)]
        dp[0][0] = True
        # initialize first row vs ''
        for j in range(1, n):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # fill the table
        for i in range(1,m):
            for j in range(1,n):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j]

        return dp[-1][-1]





s = "aab"
p = "c*a*b"
# s = "mississippi"
# p = "mis*is*p*."
sol = Solution()
print(sol.isMatch(s, p))
