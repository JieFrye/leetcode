class Solution:
    def palindromePairs(self, words):
        '''
        ideas: use dict to keep track of word: index

        abcd : 0 abcd[::-1] is dcba, it is in dict, so add [dic[word], 0]
        dcba : 1
        lls : 2  prefix '', l, ll, lls suffix lls, ls, s, ''
        s : 3
        sssll : 4

        aaaab baaaa baaa baa ba b
          pref suff
            |  |
        bot b+ot  if 'to' is there, add to the front
        pref suff
          |  |
        ban+ana: if 'nab' is there, add to the back

        Assumption: long list short words
        '''
        def isP(s):
            return s == s[::-1]

        dic = {word: i for i, word in enumerate(words)}
        pairs = []
        for word, k in dic.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                surf = word[j:]
                if isP(pref):
                    front = surf[::-1]
                    if front != word and front in dic:
                        pairs.append([dic[front], k])
                if j!= n and isP(surf):
                    back = pref[::-1]
                    if back != word and back in dic:
                        pairs.append([k, dic[back]])
        return pairs


        # brute-force solution
        # result = []
        # for i, s in enumerate(words):
        #     for j, t in enumerate(words):
        #         if i > j:
        #             if s + t == (s+t)[::-1]:
        #                 result.append([i, j])
        #             if t + s == (t+s)[::-1]:
        #                 result.append([j, i])
        # return result

words = ["abcd","dcba","lls","s","sssll"]
sol = Solution()
print(sol.palindromePairs(words))
