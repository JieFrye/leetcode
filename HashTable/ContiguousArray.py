# Given a binary array, find the maximum length of a contiguous subarray
# with equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums) -> int:
        # use a count to keep track of the trends of 0 and 1
        count = 0
        dic = { 0:0 }
        max_len = 0
        # count starts at 0, if first element is 0, count = -1
        # if first elment is 1, count = 1
        for i, e in enumerate(nums, 1):
            if e == 0:
                count -= 1
            if e == 1:
                count += 1
            if count in dic:
                max_len = max(max_len, i - dic[count])
            else:
                dic[count] = i
        return max_len

nums = [0,1,0]
sol = Solution()
print(sol.findMaxLength(nums))
