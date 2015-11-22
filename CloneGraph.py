"""
133. Clone Graph
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
"""

class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []
# O(n)
# O(n)
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return
        lookup = {}
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur.label not in lookup:
                lookup[cur.label] = UndirectedGraphNode(cur.label)
            copy = lookup[cur.label]
            for neighbor in cur.neighbors:
                if neighbor.label not in lookup:
                    lookup[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)
                copyNeighbor = lookup[neighbor.label]
                copy.neighbors.append(copyNeighbor)
        return lookup[node.label]
