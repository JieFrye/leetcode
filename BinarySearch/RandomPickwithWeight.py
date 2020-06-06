# Given an array w of positive integers,
# where w[i] describes the weight of index i,
# write a function pickIndex which randomly picks
# an index in proportion to its weight.

import random

class Solution:

    def __init__(self, w):
        '''
        find the prefix sum and total
        '''
        self.prefix_sum = []
        total = 0
        for e in w:
            total += e
            self.prefix_sum.append(total)
        self.total = total

    def pickIndex(self) -> int:
        '''
        random will give us a random number in [0, 1)
        '''
        target = random.randint(1,self.total)
        low, high = 0, len(self.prefix_sum)
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Your Solution object will be instantiated and called as such:
w = [1, 3]
obj = Solution(w)
result = []
for i in range(5):
    result.append(obj.pickIndex())
print(result)
