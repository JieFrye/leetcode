# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest
# substring (not subsequence) without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Ideas: use dict to keep track of char and
        use two pointers to move the window
        '''
        n = len(s)
        if n < 2:
            return n
        longest, w = 0, 0
        seen = {}
        for i in range(n):
            if s[i] in seen and w <= seen[s[i]]:
                # if we have seen the char, move window
                w = seen[s[i]] + 1
            else:
                # update the length of longest vs window size
                longest = max(longest, i - w + 1)
            # update dict with the unseen char: index
            seen[s[i]] = i
        return longest

# s = "abcabcbb
# s = "pwwkew"
s = "tmmzuxt"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
