# Given an array of strings, group anagrams together.

class Solution:
    def groupAnagrams(self, strs):
        '''
        input: List[str]
        output: List[List[str]]
        idea: sort each str and use dic to sort the values
        '''
        result = []
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        for k in dic:
            result.append(dic[k])
        return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
