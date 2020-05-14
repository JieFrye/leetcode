# Two Pointers
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

numbers = [1,2,7,11,15]
target = 13
def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        if target - numbers[i] == numbers[j]:
            return [i+1, j+1]
        elif target - numbers[i] < numbers[j]:
            j -= 1
        else:
            i += 1
#ans = twoSum(numbers, target)
#print(ans)

# https://leetcode.com/problems/container-with-most-water/
height = [1,8,6,2,5,4,8,3,7]
def maxArea(height) -> int:
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
print(maxArea(height))
