# DP
# in April 30-Day Challenge
# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # since the mat is sorted, we start from the top right cornor
        # if we see a 0, go down
        # if we see a 1, go left
        # time O(m+n) and space O(1)
        rows, cols = binaryMatrix.dimensions()
        row, col = 0, cols - 1
        result = -1
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                result = col
                col -= 1
            else:
                row += 1
        return result
