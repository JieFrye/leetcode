# 5/12
nums = [2,2,3,3,4]
def single(nums):
    '''
    given a sorted array consisting of only integers where every element
    appears exactly twice, except for one element which appears exactly once.
    Find this single element that appears only once.
    '''
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            i += 2
        else:
            return nums[i]
    return nums[i]

print(single(nums))
