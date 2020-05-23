#
# Given two lists of closed intervals, pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.

class Solution:
    def intervalIntersection(self, A, B):
        '''
        use two pointers to track the two intervals for intersection 
        '''
        C = []
        i = 0
        j = 0
        while i < len(A) and j <len(B):
            a = max( A[i][0], B[j][0] )
            b = min( A[i][1], B[j][1] )
            # if we have an interval or point
            if a <= b:
                C.append([a, b])
            if A[i][1] < B[j][1]:
                # move to the next A interval to find intersection
                i +=  1
            else:
                j += 1
        return C


A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
sol = Solution()
print(sol.intervalIntersection(A, B))
