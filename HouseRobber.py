# Insight Dynamic Programming
# https://leetcode.com/problems/house-robber/
nums = [2,7,9,3,1,3]

class Solution:
    def rob(self, nums) -> int:
        '''
        [2,7,9,3,1,3] ->          [2,(7), 9,   3,   1,  3]
        at 9, compare 7 and 2+9   [2, 7, (11), 3,   1,  3]
        at 3, compare 11 and 3+7  [2, 7,  11, (11), 1,  3]
        at 1, compare 11 and 1+11 [2, 7,  11,  11, (12),3]
        at 3, comapre 12 and 11+3 [2, 7,  11,  11,  12, (14)]
        '''
        prev, now = 0, 0
        for v in nums:
            prev2 = prev # the nums[i-2]th value
            prev = now # the nums[i-1]th value
            now = max(prev2 + v, prev)
        return now

sol = Solution()
print(sol.rob(nums))
