# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        Note: length of the longest valid parentheses substring (not subsequence)
        "()(()" -> 2
        '''
        # keep track of the beginning index of the valid substring
        stack = [-1]
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                # the ')' will close the last '(' so pop its index
                stack.pop()
                if stack:
                    result = max(result, i - stack[-1])
                else:
                    # stack is empty, add the beginning index of the next valid substring
                    stack.append(i)
        return result

s = "()(()"
sol = Solution()
print(sol.longestValidParentheses(s))


        # '''
        # Find minimum number of parentheses needed to valid the string
        # len(str) - min = longest (subsequence) "()(()" -> 4
        # '''
        # # keep track of p that need to be closed
        # count = 0
        # # keep track of p that can be paired
        # stack = []
        # for p in s:
        #     if stack and p == stack[-1]:
        #         stack.pop()
        #     else:
        #         if p == '(':
        #             stack.append(')')
        #         else:
        #             count += 1
        # return len(s) - (len(stack) + count)
