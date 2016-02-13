"""
222. Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(logn ^ 2)
# O(1)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth, cur = self.getDepth(root), root
        lower, upper = 2 ** (depth - 1), 2 ** depth - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if self.getDepth(cur.right) == depth - 1:
                lower = mid + 1
                cur = cur.right
            else:
                upper = mid
                cur = cur.left
            depth -= 1
        return lower
        
    def getDepth(self, node):
        depth = 0
        while node:
            depth, node = depth + 1, node.left
        return depth

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    print(Solution().countNodes(root))
