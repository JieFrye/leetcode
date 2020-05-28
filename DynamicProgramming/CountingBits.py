# Counting Bits

# Given a non negative integer number num. For every numbers i in the range
# 0 ≤ i ≤ num calculate the number of 1's in their binary representation
# and return them as an array.

# Reference: https://wiki.python.org/moin/BitwiseOperators

class Solution:
    def countBits(self, num: int):
        '''
        Observations: 7 = 0111, 6 = 0110, right shift the ones gives 0011 = 3.
        Right shift is equiv to //2.
        C[7] = 3 and C[6] = 2 while C[3] = 2.
        x >> y
        Returns x with the bits shifted to the right by y places.
        This is the same as //'ing x by 2**y.
        x & y
        Does a "bitwise and". Each bit of the output is 1 if the
        corresponding bit of x AND of y is 1, otherwise it's 0.
        '''
        C = [0]
        for i in range(1, num + 1):
            C.append( C[i >> 1] + int(i & 1) )
        return C

sol = Solution()
num = 7
print(sol.countBits(num))
