"""
261. Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.”
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
# O(n)
# O(n)
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 0:
            return True
        if n == 1 and not edges:
            return True
        lookup = {}
        for edge in edges:
            if edge[0] not in lookup:
                lookup[edge[0]] = set([edge[1]])
            else:
                lookup[edge[0]].add(edge[1])
            if edge[1] not in lookup:
                lookup[edge[1]] = set([edge[0]])
            else:
                lookup[edge[1]].add(edge[0])
        if 0 not in lookup:
            return False
        cur, visited, count = [0], [False for i in range(n)], 0
        while cur:
            next = []
            while cur:
                edge = cur.pop()
                if visited[edge]:
                    return False
                visited[edge] = True
                count += 1
                for i in lookup[edge]:
                    next.append(i)
                    lookup[i].remove(edge)
                del(lookup[edge])
            cur = next
        return count == n

if __name__ == "__main__":
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(Solution().validTree(5, edges))
    
