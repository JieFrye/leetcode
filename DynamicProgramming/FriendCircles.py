# Friend Circles
# There are N students in a class. Some of them are friends, while some are not.
# Their friendship is transitive in nature. For example, if A is a direct friend
# of B, and B is a direct friend of C, then A is an indirect friend of C.
# And we defined a friend circle is a group of students who are direct or
# indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students
# in the class. If M[i][j] = 1, then the ith and jth students are direct
# friends with each other, otherwise not. And you have to output the total
# number of friend circles among all the students.

class Solution:
    def findCircleNum(self, M) -> int:
        '''
        unlike Numer of Islands,
        the members of a circle need not be all connected
        [1,1,0,0,1]
        [1,1,0,0,0]
        [0,0,1,1,0]
        [0,0,1,1,0]
        [1,0,0,0,1]
        each row is a person's friendship info
        '''
        seen = set()
        def dfs(person_i):
            for j, friend in enumerate(M[person_i]):
                if friend and j not in seen:
                    seen.add(j)
                    dfs(j) # add more persons to seen
        circles = 0
        for i in range(len(M)):
            if i not in seen:
                seen.add(i)
                dfs(i)
                circles += 1
        return circles

M = [[1,1,0,0,1],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[1,0,0,0,1]] #2
sol = Solution()
print(sol.findCircleNum(M))
