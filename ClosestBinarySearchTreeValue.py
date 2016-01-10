"""
270. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# O(h)
# O(1)
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = float("inf")
        cur = root
        while cur:
            diff = cur.val - target
            if diff > 0:
                if diff < abs(res - target):
                    res = cur.val
                cur = cur.left
            else:
                if -diff < abs(res - target):
                    res = cur.val
                cur = cur.right
        return res

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    print(Solution().closestValue(root, 2.7))
