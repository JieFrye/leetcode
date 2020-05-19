# Write a class StockSpanner which collects daily price quotes for some stock,
# and returns the span of that stock's price for the current day.

# The span of the stock's price today is defined as the maximum number of
# consecutive days (starting from today and going backwards)
# for which the price of the stock was less than or equal to today's price.
from collections import deque

class StockSpanner:

    def __init__(self):
        '''
        use stack to order prices in DESC, (price, span)
        '''
        self.s = deque()

    def next(self, price: int) -> int:
        '''
        return: the maximum number of consecutive days
        [100, 80, 60, 70, 60, 75, 85]
        [1,   1,   1,  2,  1,
        stack = [(100,1), (80,1), (70,2), (60,1)] at 75, 1+1+2 = 4 then
        stack = [(100,1), (80,1), (75,4)]
        '''
        span = 1 # min span (price itself)
        while self.s and price >= self.s[-1][0]:
            span += self.s[-1][1]
            self.s.pop()
        self.s.append((price,span))
        return span




# Your StockSpanner object will be instantiated and called as such:
S = StockSpanner()
prices = [100, 80, 60, 70, 60, 75, 85]
L = []
for p in prices:
    L.append(S.next(p))
print(L)
print(L == [1, 1, 1, 2, 1, 4, 6])
