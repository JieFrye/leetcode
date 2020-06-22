# Single Number II

# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums) -> int:
        '''
        ideas: sort nums and use a pointer
        '''
        i = 1
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        if nums[1] != nums[0]:
            return nums[0]
        if nums[-1] != nums[n-2]:
            return nums[-1]
        while i < n:
            if nums[i-1] == nums[i]:
                i += 3
            else:
                return nums[i-1]

nums = [0,1,0,1,0,1,99]
# nums = [1]
# nums = [2,2,3,2]
# nums = [40,-15,51,-33,41,19,-5,28,-50,-12,48,-46,-26,-37,41,54,51,-29,-30,-49,29,4,-7,30,18,32,6,9,24,-15,-13,12,20,-8,6,53,18,14,-2,-46,-25,-22,-20,-46,-28,-35,18,15,-3,49,54,-20,55,28,-39,4,52,-12,37,29,-29,15,50,46,42,-22,11,43,49,40,16,-3,-13,-33,-7,25,16,-24,-34,-50,-31,-37,-50,6,44,-25,-15,25,11,47,40,41,-24,32,49,-20,-29,-33,52,-2,-49,48,-25,24,-42,-37,39,-6,-49,54,-30,-44,15,-42,-28,-22,20,25,-30,-48,-31,12,-40,20,-14,-16,-40,42,-12,46,-1,-35,-6,39,-8,-32,50,-31,43,28,32,-8,5,-3,-48,11,5,55,9,-39,-39,42,-7,33,-35,9,14,-34,53,51,-32,30,44,50,-48,-44,-6,-5,19,12,-26,-16,-13,53,33,-1,23,4,-16,37,29,16,44,19,46,-32,39,5,47,-28,37,43,52,-42,33,24,-40,30,-24,48,-34,-5,-14,47,-14,55,-26,-2,-1,-44,14]
sol = Solution()
print(sol.singleNumber(nums))
