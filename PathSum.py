"""
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(h)
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.recur(root, sum)
        
    def recur(self, root, sum):
        if root.left == root.right == None:
            if root.val == sum:
                return True
            return False
        if root.left and self.recur(root.left, sum - root.val):
            return True
        if root.right and self.recur(root.right, sum - root.val):
            return True
        return False

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().hasPathSum(root, 10))
