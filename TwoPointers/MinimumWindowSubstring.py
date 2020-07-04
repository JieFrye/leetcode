# Minimum Window Substring
# Given a string S and a string T, find the minimum window in S
# which will contain all the characters in T in complexity O(n).
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Ideas: use two pointers and hash map
        '''
        if not s or not t:
            return ''
        T = collections.Counter(t)
        S = collections.Counter()
        l, r = -1, len(s)
        i = 0
        for j in range(len(s)):
            S[s[j]] += 1
            while S & T == T:
                if j - i < r - l:
                    l, r = i, j
                S[s[i]] -= 1
                i += 1
        if r - l < len(s):
            return s[l:r+1]
        else:
            return ''

S = "ADOBECODEBANC"
T = "ABC"
sol = Solution()
print(sol.minWindow(S,T))
