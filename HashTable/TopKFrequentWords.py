# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words
# have the same freq, the word with the lower alphabetical order comes first.

# Try to solve it in O(n log k) time and O(n) extra space.

class Solution:
    def topKFrequent(self, words, k: int):
        '''
        words: List[str]
        return: List[str]
        ideas:
        use dict to record int: freq
        use another dict to record freq: [word]
        ans [word] from top freq to low in alpha order
        '''
        if k == len(words):
            words.sort()
            return words
        dic = {}
        for w in words:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] += 1
        freq = {}
        for w, f in dic.items():
            if f not in freq:
                freq[f] = [w]
            else:
                freq[f].append(w)
        for f in freq:
            freq[f].sort()
        ans = []
        for i in range(len(words), 0, -1):
            if i in freq:
                ans.extend(freq[i])
        return ans[:k]

# words = ['love', 'i']
# words = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
sol = Solution()
print(sol.topKFrequent(words, k))
