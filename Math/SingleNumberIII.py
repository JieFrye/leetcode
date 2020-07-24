# Given an array of numbers nums, in which exactly two elements appear
# only once and all the other elements appear exactly twice.
# Find the two elements that appear only once.

# Your algorithm should run in linear runtime complexity.

class Solution:
    def singleNumber(self, nums):
        '''
        ideas:
        Use XOR to get the difference of the two target elements.
        1^1 = 0 same, 1^0 = 1 different
        3^5 = 011 ^ 101 = 110
        Note that 3 and 5 differ at the second bit from right,
        n &= -n gives the last significant bit
        So group the numbers into two groups based on this difference.
        '''
        xy = 0
        x = 0
        y = 0
        for n in nums:
            xy ^= n
        # group = 1
        # while(xy & group == 0):
        #     group = group << 1
        group = xy & -xy
        for n in nums:
            if n & group:
                x ^= n
            else:
                y ^= n
        return [x, y]

nums = [1,2,1,3,2,5]
sol = Solution()
print(sol.singleNumber(nums))
