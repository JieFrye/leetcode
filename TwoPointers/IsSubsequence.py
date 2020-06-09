# Is Subsequence
# Given a string s and a string t, check if s is subsequence of t.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        ideas: use recursion or two pointers
        '''
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        # if s[0] == t[0]:
        #     return self.isSubsequence(s[1:], t[1:])
        # else:
        #     return self.isSubsequence(s, t[1:])
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False

s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))
