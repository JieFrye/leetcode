# Decode Ways
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.

class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        ideas:
        '1213' when we add the second 1, either
        1,2 + 1
        12 + 1
        or
        1 + 21
        similarly, when we add 3, either
        1,2,1 + 3
        12,1 + 3
        1,21 + 3
        or
        1,2 + 13
        12 + 13
        but 0 cannot be in the front
        '''
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        # keep track of the n-1th and n-2th terms
        one, two = 1, 1
        for i in range(1, len(s)):
            d = int(s[i])
            dd = int(s[i-1])*10 + d
            temp = 0
            if d > 0:
                temp += one
            if 10 <= dd <= 26:
                temp += two
            two = one
            one = temp
        return one

s = '1213'
sol = Solution()
print(sol.numDecodings(s))
