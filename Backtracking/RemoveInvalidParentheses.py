# Remove Invalid Parentheses
# Remove the minimum number of invalid parentheses in order to make the
# input string valid. Return all possible results.

class Solution:
    def removeInvalidParentheses(self, s: str):
        '''
        step 1: find how many ( and ) we need to remove
        step 2: use dfs to build candidates and check if s has valid ()
        '''
        # count how many ( and ) we need to remove
        l = 0
        r = 0
        for c in s:
            l += (c == '(')
            if l == 0:
                r += (c == ')')
            else:
                l -= (c == ')')
        # return answer
        ans = []
        self.dfs(s, 0, l, r, ans)
        return ans

    # pick candidates
    def dfs(self, s, start_pos, l, r, ans):
        if l ==0 and r == 0:
            if self.isValid(s):
                ans.append(s)
            return
        for i in range(start_pos, len(s)):
            # avoid duplicate
            if i != start_pos and s[i] == s[i-1]:
                continue
            if s[i] == '(' or s[i] == ')':
                # remove ) first
                if r > 0:
                    self.dfs(s[:i]+s[i+1:], i, l, r-1, ans)
                # remove ( next
                elif l > 0:
                    self.dfs(s[:i]+s[i+1:], i, l-1, r, ans)

    def isValid(self, s):
        '''
        check if s has valid ()
        '''
        count = 0
        for c in s:
            if c == '(':
                count += 1
            if c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

# s = "()())()"
# s = "(a)())()"
s = ")("
sol = Solution()
print(sol.removeInvalidParentheses(s))
