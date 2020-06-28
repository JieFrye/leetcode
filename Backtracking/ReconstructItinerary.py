# Reconstruct Itinerary
# Given a list of airline tickets represented by pairs of departure and
# arrival airports [from, to], reconstruct the itinerary in order.
# All of the tickets belong to a man who departs from JFK.
# Thus, the itinerary must begin with JFK.

# 1. If there are multiple valid itineraries, you should return the itinerary
# that has the smallest lexical order when read as a single string.
# e.g. ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# 2. All airports are represented by three capital letters (IATA code).
# 3. You may assume all tickets form at least one valid itinerary.
# 4. One must use all the tickets once and only once.
import collections

class Solution:
    def findItinerary(self, tickets):
        '''
        input: List[List[str]], output: List[str]
        ideas: use dict to store from:[list of destinations]
        '''
        if not tickets:
            return
        # group a sequence of key-value pairs into a dictionary of lists
        d = collections.defaultdict(list)
        for A, B in tickets:
            d[A].append(B)
        # the itinerary must begin with JFK
        itinerary = ["JFK"]

        def dfs(A):
            '''
            builds candidates for the solution and
            abandons those which cannot fulfill the conditions
            '''
            if len(itinerary) == len(tickets) + 1:
                return True
            destinations = sorted(d[A])
            for B in destinations:
                # perform backtracking
                itinerary.append(B)
                d[A].remove(B)
                if dfs(B):
                    return True
                # else return and try a different B
                d[A].append(B)
                itinerary.pop()
        # call the helper function to construct the list
        dfs("JFK")
        return itinerary

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
sol = Solution()
print(sol.findItinerary(tickets))
