"""
323. Number of Connected Components in an Undirected Graph
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
# O(n)
# O(n)
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        lookup = {}
        for edge in edges:
            if edge[0] not in lookup:
                lookup[edge[0]] = [edge[1]]
            else:
                lookup[edge[0]].append(edge[1])
            if edge[1] not in lookup:
                lookup[edge[1]] = [edge[0]]
            else:
                lookup[edge[1]].append(edge[0])
        res, visited = 0, [False for i in range(n)]
        for i in range(n):
            if i not in lookup:
                res += 1
                visited[i] = True
            elif not visited[i]:
                res += 1
                visited[i] = True
                self.DFS(visited, lookup, i)
        return res
        
    def DFS(self, visited, lookup, key):
        for i in lookup[key]:
            if i in lookup and not visited[i]:
                visited[i] = True
                self.DFS(visited, lookup, i)

# O(n)
# O(nlogn)
class Solution2(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        res, lookup = n, {i:i for i in range(n)}
        for edge in edges:
            root1, root2 = self.find(edge[0], lookup), self.find(edge[1], lookup)
            if root1 != root2:
                res -= 1
                self.union(root1, root2, lookup)
        return res
        
    def find(self, node, lookup):
        if lookup[node] == node:
            return node
        return self.find(lookup[node], lookup)
        
    def union(self, root1, root2, lookup):
        lookup[min(root1, root2)] = max(root1, root2)

if __name__ == "__main__":
    edges = [[0, 1], [1, 2], [3, 4]]
    print(Solution().countComponents(5, edges))
