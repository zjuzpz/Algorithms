"""
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# O(n)
# O(h)
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        cur, res = str(root.val), []
        self.recur(res, cur, root)
        return res
        
    def recur(self, res, cur, root):
        if not root.left and not root.right:
            res.append(cur)
            return
        if root.left:
            self.recur(res, cur + "->" + str(root.left.val), root.left)
        if root.right:
            self.recur(res, cur + "->" + str(root.right.val), root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    print(Solution().binaryTreePaths(root))
