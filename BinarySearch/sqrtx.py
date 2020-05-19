# https://leetcode.com/problems/sqrtx/
# Binary Search

x = 5

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x
        while i <= j:
            mid = (i + j) // 2
            if mid**2 <= x < (mid + 1)**2:
                return mid
            elif mid**2 > x:
                j = mid - 1
            else:
                i = mid + 1
        return False


sol = Solution()
print(sol.mySqrt(x))
