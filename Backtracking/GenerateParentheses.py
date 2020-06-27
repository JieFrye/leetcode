# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.


class Solution:
    def generateParenthesis(self, n: int):
        '''
        The open parenthesis goes before the close parenthesis
        n = 1 pair, ()
        n = 2 pairs, ()(), (())
        n = 3 pairs, ()-()(), ()-(()), (())-(), (-(())-),(-()()-)
        '''
        ans = []
        self.backtrack(ans, "", 0, 0, n)
        return ans

    def backtrack(self, ans_list, curr_string, count_open, count_close, pairs):
        if len(curr_string) == 2*pairs:
            # generated enough ()
            ans_list.append(curr_string)
            return
        # get enought () and always begin with (
        if count_open < pairs:
            # print('open', count_open, curr_string)
            self.backtrack(ans_list, curr_string + '(', \
                            count_open + 1, count_close, pairs)
        # ensure valid and end with )
        if count_close < count_open:
            # print('close', count_close, curr_string)
            self.backtrack(ans_list, curr_string + ')', \
                            count_open, count_close + 1, pairs)

sol = Solution()
print(sol.generateParenthesis(3))
