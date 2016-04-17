"""
298. Binary Tree Longest Consecutive Sequence
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(h)
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.recur(root, 1)
        return self.res
        
    def recur(self, root, cur):
        self.res = max(self.res, cur)
        if root.right:
            if root.val == root.right.val - 1:
                self.recur(root.right, cur + 1)
            else:
                self.recur(root.right, 1)
        if root.left:
            if root.val == root.left.val - 1:
                self.recur(root.left, cur + 1)
            else:
                self.recur(root.left, 1)

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    print(Solution().longestConsecutive(root))
