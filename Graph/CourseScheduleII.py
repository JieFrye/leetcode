# Course Schedule II
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the
# ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them.
# If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        '''
        ideas:
        use topological sort
        '''
        # find how many directed edges is pointing to each course
        degrees = [0 for _ in range(numCourses)]
        for e in prerequisites:
            degrees[e[0]] += 1
        # print(degrees)

        # use stack to keep track of 0 degrees
        stack = []
        for i in range(numCourses):
            if degrees[i] == 0:
                stack.append(i)

        # sort courses
        ans = []
        while stack:
            curr = stack.pop()
            ans.append(curr)
            for e in prerequisites:
                if e[1] == curr:
                    degrees[e[0]] -= 1
                    if degrees[e[0]] == 0:
                        stack.append(e[0])
        # print(ans)
        if len(ans) == numCourses:
            return ans
        else:
            return []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2],[1,3]]
sol = Solution()
print(sol.findOrder(numCourses, prerequisites))
