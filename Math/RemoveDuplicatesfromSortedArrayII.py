# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
#
# Do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums) -> int:
        '''
        idea: use the sorted property
        check 2 places back. If repeat, do nothing.
        Else, change the value at position.
        '''
        # i = 0
        # for n in nums:
        #     if i < 1 or n > nums[i-1]:
        #         nums[i] = n
        #         i += 1
        # return nums[:i]
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i



nums = [0,0,1,1,1,1,2,3,3]
sol = Solution()
print(sol.removeDuplicates(nums))
