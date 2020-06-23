class Solution:
    def trap(self, height) -> int:
        '''
        ideas: use two pointers
        '''
        n = len(height)
        V = 0
        if not height or n < 3:
            return V
        i, j = 0, n - 1
        l, r = height[i], height[j]
        while i < j:
            l = max(height[i], l)
            r = max(height[j], r)
            if l <= r:
                V += l - height[i]
                i += 1
                print(i)
            else:
                V += r - height[j]
                j -= 1
                print(j)
        return V


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [0,1,2,3,4]
# height = [3,2,1,0,1,2,3,3,2,1,0,1,2,3]
sol = Solution()
print(sol.trap(height))
