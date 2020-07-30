# Word Break II
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word
# is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

class Solution:
    def wordBreak(self, s: str, wordDict):
        '''
        use recoursion
        "catsanddog" = 'cat' + wordBreak("sanddog")
        use DP to deal with
        "aaaaaaa" and {'a', 'aa', 'aaa'} because
        "aaaaaaa" = 'a' + 'a' + wordBreak("aaaaa")
        "aaaaaaa" = 'aa' + wordBreak("aaaaa")
        '''
        result = []
        for w in wordDict:
            if s[:len(w)] == w:
                if len(w) == len(s):
                    result.append(w)
                else:
                    temp = self.wordBreak(s[len(w):], wordDict)
                    for t in temp:
                        result.append(w + " " + t)
        return result

s = "catsanddog"
words = ["cat", "cats", "and", "sand", "dog"]
sol = Solution()
print(sol.wordBreak(s, words))
