# Given a non-empty array of integers, return the k most frequent elements.
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of
# the top k frequent elements is unique.
# You can return the answer in any order.


class Solution:
    def topKFrequent(self, nums, k: int):
        '''
        ideas:
        use dict to record int: freq
        use another dict to record freq: [int]
        ans [int] from top freq to low
        '''
        if k == len(nums):
            return nums
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        freq = {}
        for n, f in dic.items():
            if f not in freq:
                freq[f] = [n]
            else:
                freq[f].append(n)
        ans = []
        for i in range(len(nums), 0, -1):
            if i in freq:
                ans.extend(freq[i])
        return ans[:k]

nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))
