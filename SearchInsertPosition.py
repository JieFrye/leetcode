# https://leetcode.com/problems/search-insert-position/
# Binary Search

nums = [1,3,5,6]
target = 4

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1 # -1 becuase nums[mid] already != target
            else:
                i = mid + 1
        # if while loop ends without return target is not in sorted array
        # target is smaller so insert it here
        if nums[mid] > target:
            return mid
        # target is greater so insert it in next index
        else:
            return mid + 1


sol = Solution()
print(sol.searchInsert(nums, target))
