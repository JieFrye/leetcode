# LettCode May 17 2020 Challenge

s = "aaaababcac"
p = "ababc"

class Solution:
    def findAnagrams(self, s: str, p: str):
        '''
        Given a string s and a non-empty string p,
        find all the start indices of p's anagrams in s.
        '''
        L, window, slen = [], len(p), len(s)
        # if s is not long enough to make anagrams
        if slen < window:
            return L
        # count the char in p
        pdic = {}
        for l in p:
            if l in pdic:
                pdic[l] += 1
            else:
                pdic[l] = 1
        # count the char in s in each window
        sdic = {}
        for i in range(slen):
            if s[i] in sdic:
                sdic[s[i]] += 1
            else:
                sdic[s[i]] = 1
            if i >= window: # ensure sdic counts char within window
                if sdic[s[i-window]] == 1:
                    # delete key that will have zero count
                    del sdic[s[i-window]]
                else:
                    # decrease the key count as the window move
                    sdic[s[i-window]] -= 1
            if sdic == pdic:
                L.append(i-window+1)
        return L




sol = Solution()
ans = sol.findAnagrams(s, p)
print(ans)
