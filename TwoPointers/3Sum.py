# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which
# gives the sum of zero.
#
# Note:
# The solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums):
        '''
        Input: nums: List[int]
        Output: List[List[int]]
        Ideas:
        iterate thro every number in nums and
        use two pointers to find its friends
        '''
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0:
                # all positive numbers
                return ans
            if i > 0 and nums[i]==nums[i-1]:
                # solution set must not contain duplicate triplets
                continue
            # combination from 0 to i has been tried
            l, r = i+1, n-1
            # move two pointers to find friends
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: # need larger friends
                    l += 1
                elif s > 0: # need smaller friends
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # loop thro all the repeated numbers
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    # move to the next set of (different) friends
                    l += 1
                    r -= 1
        return ans

nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))
