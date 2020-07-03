# First Missing Positive
# Given an unsorted integer array, find the smallest missing positive integer.

class Solution:
    def firstMissingPositive(self, nums) -> int:
        '''
        ideas: min missing positive integer is in the range(1, n+1)
        e.g. [1,2,3] -> 4
        '''
        nums.append(0)
        n = len(nums)
        # delete numbers that are out side [1, len(nmus)+1]
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        # use index as the hash to record freq
        for i in range(n):
            nums[nums[i]%n] += n
        # the index at missing integer is never updated
        print(nums)
        for i in range(1,n):
            if nums[i]//n == 0:
                return i
        return n

# nums = [7,8,9,11,12]
# nums = [4,5,2,1]
nums = [1,2,4]
sol = Solution()
print(sol.firstMissingPositive(nums))
