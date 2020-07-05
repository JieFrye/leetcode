# Ugly Number II
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        ideas: 2^i3^j5^k
        '''
        nums = [1]
        i = 0
        j = 0
        k = 0
        while len(nums) < n:
            temp2 = nums[i]*2
            temp3 = nums[j]*3
            temp5 = nums[k]*5
            ugly = min(temp2, temp3, temp5)
            nums.append(ugly)
            if ugly == temp2:
                i += 1
            if ugly == temp3:
                j += 1
            if ugly == temp5:
                k += 1
        return nums[-1]

n = 10
sol = Solution()
print(sol.nthUglyNumber(n))
