# Stack & Queue
# https://leetcode.com/problems/valid-parentheses/
from collections import deque

class Solution:

    def isValid(self, s: str) -> bool:
        '''
        use stack to keep track of what needs to be closed next
        use dict to store the pairs
        '''
        stack = deque()
        dic = {"(":")", "[":"]", "{":"}"}
        for p in s:
            if p in dic.keys(): # an open parenthese
                stack.append(dic[p]) # it is next to be closed
            elif p in dic.values(): # a closed parenthese
                if stack == deque() or p != stack.pop():
                    # if it is not closing the last item
                    return False
            else: # not a parenthese
                return False
        return stack == deque()

sol = Solution()
#s = "([)]"
#s = "()[]{}"
s = "{[]}"
print(sol.isValid(s))
