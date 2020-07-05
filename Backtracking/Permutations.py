# Given a collection of distinct integers, return all possible permutations.

class Solution:
    def permute(self, nums):
        '''
        ideas: keep track of each i and permute the rest
        use backtracking to build candidates
        '''
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result):
        if not nums:
            # add new permutation to the result
            result.append(path)
        # broke down all possibilities into path
        for i in range(len(nums)):
            # take out the ith element until nums is exhausted
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)

nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))
