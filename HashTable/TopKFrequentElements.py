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
