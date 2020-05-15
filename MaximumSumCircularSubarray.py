# 5/15 May Challenge
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/

#A = [1,-2,3,-2] #3
#A = [5,-3,5] #10
#A = [3,-1,2,-1] #4
#A = [3,-2,2,-3] #3
#A = [-2,-3,-1] #-1
A = [1,2,3,4,5] #15

def maxSubarraySumCircular(A) -> int:
    '''
    Kadane's algorithm Dynamic Programming
    ans = float('-inf')
    dp = A[0]
    for i in range(len(A)):
        dp = max(dp, 0) + A[i]
        ans = max(ans, dp)
    return ans
    Case 1: if max subarray is straight, then Kadane
    Case 2: if max subarray is circular, the partition A into A1, A2, A3
    maxcs = A1+A3 = sum - A2
    [5, -3, 5]  maxcs = 5+5
    [-5, 3, -5] maxcs = 3, sum = 7, maxcs = sum - (-3) mincs
    non-empty subarray requires sum != - mincs
    '''
    k = Kadane(A)
    s = 0
    for i in range(len(A)):
        s += A[i] # get the sum of the array
        A[i] = - A[i] # negate the array
    cs = s + Kadane(A)
    if cs > k and cs != 0:
    # cs = 0 means mincs is the entire array, we need nonempty
        return cs
    else:
        return k


def Kadane(A):
    maxs, dp = A[0], A[0]
    for v in A[1:]:
        dp = max(dp, 0) + v
        maxs = max(maxs, dp)
    return maxs

print(maxSubarraySumCircular(A))
