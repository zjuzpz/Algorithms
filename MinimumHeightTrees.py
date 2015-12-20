"""
310. Minimum Height Trees
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
"""
# O(n)
# O(n)
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        lookup = {i : set() for i in range(n)}
        for edge in edges:
            lookup[edge[0]].add(edge[1])
            lookup[edge[1]].add(edge[0])
        cur, unvisited = [], set()
        for key in lookup:
            if len(lookup[key]) == 1:
                cur.append(key)
            unvisited.add(key)
        while len(unvisited) > 2:
            next_turn = []
            for key in cur:
                unvisited.remove(key)
                for node in lookup[key]:
                    lookup[node].remove(key)
                    if node in unvisited and len(lookup[node]) == 1:
                        next_turn.append(node)
            cur = next_turn
        return list(unvisited)

if __name__ == "__main__":
    n = 8
    edges = [[0, 3], [6, 4], [5, 7], [2, 3], [2, 4], [2, 5], [2, 1]]
    print(Solution().findMinHeightTrees(n, edges))
