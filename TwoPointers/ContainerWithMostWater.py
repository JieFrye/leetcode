class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        we want the container to be wide and tall
        '''
        area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = max(area, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            # looped thro all possible width
        return area
