# Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.


class Solution:
    def merge(self, intervals):
        '''
        Input and Output: List[List[int]]
        ideas:
        sort the intervals by the left end points
        merge the intervals or add to result
        '''
        result = []
        intervals.sort(key=lambda x: x[0])
        # [[1,3],[2,6],[8,10],[9,18]]
        for i in intervals:
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)
        return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()
print(sol.merge(intervals))
