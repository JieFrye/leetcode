# Say you have an array for which the ith element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time
# (you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (cooldown 1 day)

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        # state A: hold or buy
        A = 0
        # after buy, state B: hold or sell
        B = -prices[0]
        # after sell: state C: hold
        C = 0
        for i in range(1, len(prices)):
            preA = A
            A = max(A, C)
            C = B + prices[i]
            B = max(B, preA - prices[i])
        return max(A, C) # either hold or sell at the end


prices = [1,2,3,0,2] # 3 [buy, sell, cooldown, buy, sell]
sol = Solution()
print(sol.maxProfit(prices))
