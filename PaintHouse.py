"""
256. Paint House
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
"""
# O(n)
# O(1)
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        cur, next = costs[0], [0, 0, 0]
        for i in range(1, len(costs)):
            next[0] = costs[i][0] + min(cur[1], cur[2])
            next[1] = costs[i][1] + min(cur[0], cur[2])
            next[2] = costs[i][2] + min(cur[0], cur[1])
            cur = next[:]
        return min(cur)

if __name__ == "__main__":
    costs = [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
    print(Solution().minCost(costs))
