# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# we get the following ordered sequence for n = 3:
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''
        Ideas:
        Each digit in [1, n] leads (n-1)! n-permutations.
        Reduce (n, k)-case to (n-1, k%(n-1)!)-case.
        '''
        factorials = [1 for i in range(n-1)]
        for i in range(1, n-1):
            factorials[i] = factorials[i-1]*(i+1)
        digits = [i+1 for i in range(n)]
        ans = ""
        while len(ans) < n-1:
            # size of the (n-1)! permutations ordered by the leading digits
            group = factorials[-1]
            # k-1 ensure landing on correct leading digit 
            leading = (k-1)//group
            ans += str(digits[leading])
            # update perameters
            digits.pop(leading)
            factorials = factorials[:-1]
            k = k % group
            if k == 0:
                # last permutation in the group
                for i in range(len(digits)-1, -1, -1):
                    ans += str(digits[i])
        # last digit left
        if len(ans) < n:
            ans += str(digits[0])
        return ans
n = 3
k = 2
# n = 4
# k = 9
sol = Solution()
print(sol.getPermutation(n, k))
