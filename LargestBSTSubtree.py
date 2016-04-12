"""
333. Largest BST Subtree
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.
Show Hint 
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(h)
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]
        
    def helper(self, node):
        if not node:
            return (0, float("inf"), -float("inf"))
        left, right = self.helper(node.left), self.helper(node.right)
        if left[2] < node.val < right[1]:
            return (left[0] + right[0] + 1, min(left[1], node.val), max(right[2], node.val))
        return (max(left[0], right[0]), -float("inf"), float("inf"))

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().largestBSTSubtree(root))
