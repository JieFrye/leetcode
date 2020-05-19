# LeetCode May 18 Challenge
# Given two strings s1 and s2, write a function to
# return true if s2 contains the permutation of s1.

s1 = "abc"
s2 = "eidbacooo"

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        if len(s2) < window:
            return False
        pdic = {}
        for l in s1:
            if l in pdic:
                pdic[l] += 1
            else:
                pdic[l] = 1
        sdic ={}
        for i, l in enumerate(s2):
            if l in sdic:
                sdic[l] += 1
            else:
                sdic[l] = 1
            if i >= window:
                if sdic[s2[i-window]] == 1:
                    del sdic[s2[i-window]]
                else:
                    sdic[s2[i-window]] -= 1
            if pdic == sdic:
                return True
        return False

sol = Solution()
print(sol.checkInclusion(s1, s2))
