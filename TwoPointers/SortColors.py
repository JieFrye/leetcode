# Sort Colors
# Given an array with n objects colored red, white or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red,
# white, and blue respectively.

class Solution:
    def sortColors(self, nums) -> None:
        """
        nums: List[int]
        Do not return anything, modify nums in-place instead.

        ideas: put red 0 and blue 2 in their correct positions.
        use a pointer s to go thro the entire array,
        switch with l when value is 0 and r when value is 2.
        """
        s = 0
        l = 0
        r = len(nums) - 1
        while s <= r:
            if nums[s] == 0:
                nums[l], nums[s] = nums[s], nums[l]
                l += 1
                s += 1
            elif nums[s] == 2:
                nums[s], nums[r] = nums[r], nums[s]
                r -= 1
            else:
                s += 1
        return nums
sol = Solution()
# nums = [2,0,2,1,1,0]
nums = [2,0,1]
print(sol.sortColors(nums))
