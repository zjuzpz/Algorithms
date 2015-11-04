"""
104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.
"""
# O(n)
# O(h)
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.recur(root, 1)
        
    def recur(self, root, depth):
        if not root.left and not root.right:
            return depth
        if not root.left:
            return self.recur(root.right, depth + 1)
        if not root.right:
            return self.recur(root.left, depth + 1)
        return max(self.recur(root.right, depth + 1), self.recur(root.left, depth + 1))

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(Solution().maxDepth(root))
    
