# Given an integer array, count element x if x+1 is also in array

class Solution:
    def countElements(self, arr):
        '''
        [1,2,3] 1 and 2 are counted because 1+1 and 2+1 are in the array
        [1,1,2,2] 1 and 1 are counted because 1+1 and 1+1 are in the array
        O(1) lookup of the dict vs  O(n) time for linear search over the list
        '''
        dic = {}
        for x in arr:
            dic[x] = 1
        count = 0
        for x in arr:
            if x + 1 in dic:
                count += 1
        return count

arr = [1,1,2,3]
sol = Solution()
print(sol.countElements(arr))
