"""
314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,20,4,5,2,7],
    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(n)
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        lookup = {}
        cur = [(root, 0)]
        while cur:
            next = []
            for node in cur:
                if node[1] not in lookup:
                    lookup[node[1]] = []
                lookup[node[1]].append(node[0].val)
                if node[0].left:
                    next.append((node[0].left, node[1] - 1))
                if node[0].right:
                    next.append((node[0].right, node[1] + 1))
            cur = next
        visited = []
        for key in lookup:
            visited.append(key)
        visited.sort()
        res = []
        for i in visited:
            res.append(lookup[i])
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(10)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().verticalOrder(root))
