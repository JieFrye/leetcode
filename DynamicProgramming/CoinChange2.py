# Coin Change 2
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up the amount.
# You may assume that you have infinite number of each kind of coin.

class Solution:
    def change(self, amount, coins) -> int:
        '''
        amount: int
        coins: List[int]
        idea: with 1 in coins, there is only one way to make up from 0 to 5
        with 1 and 2 in coins, we either use 2 or not use 2, so
        so number of ways += dp[x - 2] for x from 2 to 5.
        '''
        # populate from 0 to amount for combos to make up such number with coins
        dp = [0] * (amount + 1)
        # to make up 0, there is 1 way: do not use the coins
        dp[0] = 1
        # consider
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[-1]

sol = Solution()
# amount = 5
# coins = [1, 2, 5]
amount = 3
coins = [2]
print(sol.change(amount, coins))
