# Given a string, sort it in decreasing order based on the freq of char.
# https://wiki.python.org/moin/HowTo/Sorting

class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        idea: use dict for freq and use lambda to sort
        '''
        dic = {}
        S = ''
        for l in s:
            if l in dic:
                dic[l] += 1
            else:
                dic[l] = 1
        s = sorted(dic, key=lambda x: dic[x], reverse=True)
        for char in s:
            S += char * dic[char]
        return S

s = "Aabb"
sol = Solution()
print(sol.frequencySort(s))
