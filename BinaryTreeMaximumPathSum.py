"""
124. Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(h)
class Solution(object):
    res = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.recur(root)
        return self.res
        
    def recur(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            self.res = max(self.res, root.val)
            return root.val
        if not root.left:
            right = self.recur(root.right)
            self.res = max(self.res, root.val, root.val + right, right)
            return max(root.val, root.val + right)
        if not root.right:
            left = self.recur(root.left)
            self.res = max(self.res, root.val, root.val + left, left)
            return max(root.val, root.val + left)
        left = self.recur(root.left)
        right = self.recur(root.right)
        self.res = max(self.res, root.val, root.val + left, root.val + right, root.val + left + right, left, right)
        return max(root.val, root.val + left, root.val + right)

# Same algorithm, simplified code:
class Solution(object):
    res = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.recur(root)
        return self.res
        
    def recur(self, root):
        if not root:
            return 0
        left = max(0, self.recur(root.left))
        right = max(0, self.recur(root.right))
        self.res = max(self.res, root.val + left + right)
        return max(root.val + left, root.val + right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().maxPathSum(root))
