# Kth Largest Element in an Array

# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        '''
        ideas:
        O(nlogn) time sort
        O(nlogk) time min-heap
        O(n) quick sort and partition
        '''
        # return sorted(nums, reverse=True)[k-1]
        if k == 1:
            return max(nums)
        if k == len(nums):
            return min(nums)
        return self.findKthSmallest(nums, len(nums)-k+1)

    def findKthSmallest(self,nums,k):
        '''
        return the kth smallest element in nums
        '''
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos + 1: # [2,1,(3),5,6,4] pos=2 k=4
                return self.findKthSmallest(nums[pos+1:],k-pos-1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos],k)
            else:
                return nums[pos]


    def partition(self, nums, l, r):
        '''
        return the position of the pivot element
        func choose the last element as pivot
        and organize the list with pivot
         p l       r
        [4,2,1,5,6,3]
        '''
        pivot_pos = l
        while l < r:
            if nums[l] < nums[r]:
                # 4 > 3 so move l to the next position
                # nothing needed to be moved to pivot_pos
                nums[l], nums[pivot_pos] = nums[pivot_pos], nums[l]
                pivot_pos += 1 # it bound the pos for nums < 3
            l += 1 #j
        # [2,1,4,5,6,3]
        nums[pivot_pos], nums[r] = nums[r], nums[pivot_pos]
        # [2,1,(3),5,6,4]
        return pivot_pos




nums = [3,2,3,1,2,4,5,5,6]
k = 4
sol = Solution()
print(sol.findKthLargest(nums, k))
