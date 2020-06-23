# Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        ideas: increase a string by 1 character can only increase the length of
        maxPalindrome by 1 or 2
        use s == s[::-1] to check Palindrome
        '''
        if len(s) == 1:
            return s
        maxlen = 1
        sindex = 0
        for i in range(len(s)):
            # if index i is at least one away from len of current max Palindrome
            # adding 1 char may increase the length by 2
            if i - maxlen >= 1 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
                sindex = i-maxlen-1
                maxlen += 2
                continue
            # if index i is zero away from len of current max Palindrome
            # adding 1 char may increase the length by 1
            if i - maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
                sindex = i-maxlen
                maxlen += 1
        return s[sindex:sindex+maxlen]


s = "babad"
# s = "cbbd"
# s = 'bacabab'
# s = 'abc'
sol = Solution()
print(sol.longestPalindrome(s))
