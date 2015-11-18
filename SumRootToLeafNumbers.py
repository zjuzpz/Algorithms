"""
129. Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(h)
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        return self.findPath(res, root, "")
        
    def findPath(self, res, root, cur):
        if not root:
            return 0
        cur += str(root.val)
        if not root.left and not root.right:
            res += int(cur)
            return res
        return self.findPath(res, root.left, cur) + self.findPath(res, root.right, cur)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().sumNumbers(root))
