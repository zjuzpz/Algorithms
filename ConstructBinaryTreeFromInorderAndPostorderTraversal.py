"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.
"""
# O(n)
# O(n)
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i
        return self.recur(lookup, postorder, 0, len(inorder), len(inorder))
        
    def recur(self, lookup, postorder, in_start, in_end, end):
        if in_start == in_end:
            return None
        val = postorder[end - 1]
        node = TreeNode(val)
        node.left = self.recur(lookup, postorder, in_start, lookup[val], end - (in_end - lookup[val] - 1) - 1)
        node.right = self.recur(lookup, postorder, lookup[val] + 1, in_end, end - 1)
        return node

if __name__ == "__main__":
    root = Solution().buildTree([1, 2], [2, 1])
    print(root.val, root.right.val)
