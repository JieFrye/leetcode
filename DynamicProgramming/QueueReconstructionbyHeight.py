# Suppose you have a random list of people standing in a queue.
# Each person is described by a pair of integers (h, k),
# where h is the height of the person and k is the number of people in front
# of this person who have a height greater than or equal to h.
# Write an algorithm to reconstruct the queue.

class Solution(object):
    def reconstructQueue(self, people):
        '''
        people: List[List[int]]
        rtype: List[List[int]]
        '''
        # sort people in descending height h and ascending position k
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        # since shorter person is irrelevant for taller ones,
        # we insert(index, p) taller persons first
        q = []
        for p in people:
            q.insert(p[1], p)
        return q

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sol = Solution()
print(sol.reconstructQueue(people))
