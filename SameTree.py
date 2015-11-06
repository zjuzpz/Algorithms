"""
100. Same Tree
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical
and the nodes have the same value.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(h)
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

if __name__ == "__main__":
    p = TreeNode(0)
    p.left = TreeNode(1)
    p.right = TreeNode(2)
    p.right.right = TreeNode(3)
    q = TreeNode(0)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    q.right.left = TreeNode(3)
    print(Solution().isSameTree(p, q))
