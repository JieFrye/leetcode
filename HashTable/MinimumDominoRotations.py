# Minimum Domino Rotations For Equal Row
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
#
# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
#
# If it cannot be done, return -1.
from collections import defaultdict

class Solution:
	def minDominoRotations(self, A, B) -> int:
		'''
		Ideas:
		Take advantage of the note 1 <= A[i], B[i] <= 6
		Use dic for number: count
		No need to worry about the position.
		If count_a + count_b - same = n, we have a match.
		'''
		n = len(A)
		if len(B) != n:
			return -1
		count_a = defaultdict(int)
		count_b = defaultdict(int)
		same = 0
		# count the frequency of each numbers from 1 to 6 in A and B
		for i in range(n):
			count_a[A[i]] += 1
			count_b[B[i]] += 1
			if A[i] == B[i]:
				same += 1
		# if one of the numbers 1 to 6 is the target value
		print(count_a, count_b)
		for x in range(1,7):
			if (count_a[x] + count_b[x] - same) == n:
				return n - max(count_a[x], count_b[x])
		# none of the numbers is the target value
		return -1

A = [2,2,4,3]
B = [2,3,2,2]
sol = Solution()
print(sol.minDominoRotations(A, B))
