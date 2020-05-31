# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character

# DP

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Ideas: dynamic programming
            '' r  o  s
        ''  0  1  2  3 # convert '' to 'r' takes 1 op then 'ro' takes 2 ops
        h   1  1  2  3 # 'h' to 'ros' replace then insert
        o   2  2  1  2 # 'ho' -> 'ro' take diag value
        r   3  2  2  2 # 'r' and 'o' diff so take min of 3 corners + 1
        s   4  3  3  2
        e   5  4  4  3
        '''
        row = len(word1)
        col = len(word2)
        dp = [[0 for j in range(col+1)] for i in range(row+1)]
        for i in range(row+1):
            for j in range(col+1):
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

sol = Solution()
# word1 = "horse"
# word2 = "ros"
word1 = "intention"
word2 = "execution"
print(sol.minDistance(word1, word2))
