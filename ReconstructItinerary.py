"""
332. Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""
# O(k1! + k2! + ... + ki!) where ki = len(lookup[place_i])
# O(n)
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        lookup, res, visited = {}, ["JFK"], {}
        for ticket in tickets:
            if ticket[0] not in lookup:
                lookup[ticket[0]] = []
                visited[ticket[0]] = []
            lookup[ticket[0]].append(ticket[1])
            visited[ticket[0]].append(False)
        for key in lookup:
            lookup[key].sort()
        for i in range(len(lookup["JFK"])):
            res.append(lookup["JFK"][i])
            visited["JFK"][i] = True
            if self.recur(res, visited, lookup, lookup["JFK"][i], len(tickets) + 1):
                return res
            visited["JFK"][i] = False
            res.pop()
            
    def recur(self, res, visited, lookup, now, expect):
        if len(res) == expect:
            return True
        if now not in lookup:
            return False
        for i in range(len(lookup[now])):
            if not visited[now][i]:
                res.append(lookup[now][i])
                visited[now][i] = True
                if self.recur(res, visited, lookup, lookup[now][i], expect):
                    return True
                visited[now][i] = False
                res.pop()
        return False

if __name__ == "__main__":
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(Solution().findItinerary(tickets))
