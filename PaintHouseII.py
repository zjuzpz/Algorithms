"""
265. Paint House II
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
"""
# O(n * k)
# O(k)
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        cur = costs[0]
        next = [0 for i in costs[0]]
        for i in range(1, len(costs)):
            first, second = float("inf"), float("inf")
            for j in range(len(cur)):
                if cur[j] < first:
                    second, first = first, cur[j]
                elif cur[j] < second:
                    second = cur[j]
            for j in range(len(cur)):
                if cur[j] == first:
                    next[j] = costs[i][j] + second
                else:
                    next[j] = costs[i][j] + first
            cur = next[:]
        return min(cur)

if __name__ == "__main__":
    costs = [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
    print(Solution().minCostII(costs))
