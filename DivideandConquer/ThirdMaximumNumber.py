# Third Maximum Number
# Given a non-empty array of integers, return the 3rd max distinct number
# in the array. If it does not exist, return the maximum number.
# The time complexity must be in O(n).

class Solution:
    def thirdMax(self, nums) -> int:
        '''
        ideas:
        delete the largest 2 numbers then get max
        '''
        # nums = set(nums)
        # if len(nums) < 3:
        #     return max(nums)
        # nums.remove(max(nums))
        # nums.remove(max(nums))
        # return max(nums)
        '''
        use quick sort or heap to scale to Kth largest
        '''
        


nums = [2, 2, 3, 1] # 1
sol = Solution()
print(sol.thirdMax(nums))
