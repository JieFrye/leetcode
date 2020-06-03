# Two City Scheduling
# There are 2N people a company is planning to interview.
# The cost of flying the i-th person to city A is costs[i][0],
# and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that
# exactly N people arrive in each city.

class Solution:
    def twoCitySchedCost(self, costs) -> int:
        # sort costs by the difference in prices
        scost = sorted(costs, key = lambda x:x[0]-x[1])
        total = 0
        for i in range(len(costs)):
            if i < len(costs)/2:
            # cheaper to go to A
                total += scost[i][0]
            else:
            # cheapter to go to B
                total += scost[i][1]
        return total

sol = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
print(sol.twoCitySchedCost(costs))
