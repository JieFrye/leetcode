# https://leetcode.com/problems/possible-bipartition/
# Similar to https://leetcode.com/problems/is-graph-bipartite/

# Given a set of N people (numbered 1, 2, ..., N),
# we would like to split everyone into two groups of any size
# Each person may dislike some other, and they can not go into the same group.

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put
# the people numbered a and b into the same group.
# Return true iff it is possible to split everyone into two groups in this way.

class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        '''
        Consider bipartite graph.
        A graph is bipartite if and only if it contains no odd cycles.
        We use 2 coloring to detect odd cycles.
        '''
        # use dic of vertex: set(dislake vertices) to store the edges
        edges = {}
        for l in dislikes:
            if l[0] not in edges:
                edges[l[0]] = set([l[1]]) # 'int' object is not iterable
            else:
                edges[l[0]].add(l[1])
            if l[1] not in edges:
                edges[l[1]] = set([l[0]])
            else:
                edges[l[1]].add(l[0])
        print(edges)
        # use dic of vertex: color to keep track of the coloring
        colors = {}
        for i in range(1, N+1):
            if i not in colors:
                colors[i] = 1 # colors are 1 or 0
                q = [i] # use queue to keep track of the next vertex
                while q:
                    a = q.pop(0)
                    if a in edges:
                        for b in edges[a]:
                            if b in colors:
                                if colors[b] == colors[a]:
                                    return False
                            else:
                                colors[b] = 1 - colors[a]
                                q.append(b)
        return True


sol = Solution()
# N = 4
# dislikes = [[1,2],[1,3],[2,4]]
# N = 3
# dislikes = [[1,2],[1,3],[2,3]]
N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print(sol.possibleBipartition(N, dislikes))
