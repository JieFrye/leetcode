# Binary Search 
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

nums1 = [1,1,2,3,3]
nums2 = [1,3,3]

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        '''
        median of even len is at mid = even // 2
        median of odd len is the average of (mid - 1) and mid elements
        '''
        l = len(nums1) + len(nums2)
        mid = l // 2
        if l % 2 == 1:
            return self.kth(nums1, nums2, mid)
        else:
            return (self.kth(nums1, nums2, mid)+self.kth(nums1, nums2, mid-1))/2

    def kth(self, A, B, k):
        '''
        find the kth element of two sorted array
        only for middle elements
        '''
        # make A shorter than B
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        # if k is the last index in merged AB
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i # by def of mid, j = len(B) // 2
        if A[i] < B[j]:
            # [1, Ai] + [3, Bj, 5]
            # AB [1, .. Ai, .. Bj, .. 5]
            # half of B is larger
            return self.kth(A[i:], B[:j], j)
        else:
            # [5, Ai, 7] + [2, 3, Bj, 5, 6]
            # AB [2, 3, .. Bj, .. Ai, .. 7]
            # half of A is larger
            return self.kth(A[:i], B[j:], i)

sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))
