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
        if not root:
            return True
        left, right = self.findDepth(root.left, 1), self.findDepth(root.right, 1)
        if left is not False and right is not False and -1 <= left - right <= 1:
            return True
        return False
        
    def findDepth(self, root, depth):
        if not root:
            return depth
        left, right = self.findDepth(root.left, depth + 1), self.findDepth(root.right, depth + 1)
        if left is not False and right is not False and -1 <= left - right <= 1:
            return max(left, right)
        return False

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().isBalanced(root))
