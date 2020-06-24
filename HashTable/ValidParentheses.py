# Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution:

    def isValid(self, s: str) -> bool:
        '''
        use stack to keep track of what needs to be closed next
        use dict to store the pairs
        '''
        stack = []
        dic = {"(":")", "[":"]", "{":"}"}
        for p in s:
            # an open parenthese
            if p in dic.keys():
                # it is next to be closed
                stack.append(dic[p])
            # a closed parenthese
            elif p in dic.values():
                # if it is not closing the last item
                if stack == [] or p != stack.pop():
                    return False
            # not a parenthese
            else:
                return False
        return stack == []

# s = "()[]{}"
s = "([)]"
sol = Solution()
print(sol.isValid(s))
