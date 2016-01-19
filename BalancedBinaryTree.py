"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(h)
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return False if self.recur(root, 0) is False else True
        
    def recur(self, node, depth):
        if not node:
            return depth
        left = self.recur(node.left, depth + 1)
        right = self.recur(node.right, depth + 1)
        if left is False or right is False:
            return False
        if abs(left - right) > 1:
            return False
        return max(left, right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().isBalanced(root))
