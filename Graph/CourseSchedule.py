# There are a total of numCourses courses you have to take,
# labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?

# Similar to Deadlock detection (single resource instance distributed system)
# Also see Kahn’s algorithm for Topological Sorting for DAG



class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        '''
        Ideas: we can reduce the problem to finding a cycle in a graph
        '''
        # first make adjacency matrix (directed graph)
        graph = [[] for i in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        # not visited 0, processing -1, processed 1
        visit = [0 for _ in range(numCourses)]
        # traverse the vertices
        def dfs(i):
            '''
            '''
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            # change not visited to processing
            visit[i] = -1
            # iterate through all neighbouring vertices
            for j in graph[i]:
                if not dfs(j):
                    return False
            # processed
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


sol = Solution()
# numCourses = 2
# prerequisites = [[1,0]]
numCourses = 4
prerequisites = [[0,1],[1,2],[2,3]]
# 0 -> 1, 1 -> 2, 2 -> 3
print(sol.canFinish(numCourses, prerequisites))
