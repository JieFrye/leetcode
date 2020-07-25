# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
#
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.

class Solution:
    def allPathsSourceTarget(self, graph):
        '''
        ideas:
        use dfs
        '''
        ans = []
        def dfs(path, i):
            if i == len(graph) - 1:
                ans.append(path + [i])
            else:
                for j in graph[i]:
                    dfs(path + [i], j)
        dfs([], 0)
        return ans


graph = [[1,2], [3], [3], []]
sol = Solution()
print(sol.allPathsSourceTarget(graph))
