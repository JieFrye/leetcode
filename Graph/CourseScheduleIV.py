# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have direct prerequisites, for example, to take course 0 you
# have first to take course 1, which is expressed as a pair: [1,0]
#
# Given the total number of courses n, a list of direct prerequisite pairs and
# a list of queries pairs.
#
# You should answer for each queries[i] whether the course queries[i][0] is a
# prerequisite of the course queries[i][1] or not.
#
# Return a list of boolean, the answers to the given queries.
#
# Please note that if course a is a prerequisite of course b and course b is a
# prerequisite of course c, then, course a is a prerequisite of course c.


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        '''
        Output List[bool]
        Use Floyd-Warshall DP O(n^3) time and O(n^2) space to set up and O(1) query
        '''
        dp = [ [False for j in range(n)] for i in range(n)]

        for i, j in prerequisites:
            dp[i][j] = True

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # either i->j or i->k->j
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])

        return [dp[i][j] for i,j in queries]

n = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
# Output: [True, False, True, False]
sol = Solution()
print(sol.checkIfPrerequisite(n,prerequisites,queries))
