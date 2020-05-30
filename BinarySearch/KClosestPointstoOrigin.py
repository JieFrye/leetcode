# K Closest Points to Origin

class Solution:
    def kClosest(self, points, K: int):
        '''
        Use the distance formula sqrt(x^2 + y^2),
        then sort the distances.
        Since we are interested in the order, no need for sqrt.
        '''
        # use tuple to pair point with distance
        distances = [ (p[0]**2+p[1]**2, p) for p in points]
        return [p for d, p in sorted(distances)[:K]]

points = [[3,3],[5,-1],[-2,4]]
K = 2
sol = Solution()
print(sol.kClosest(points, K))
