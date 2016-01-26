"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(n)
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i
        return self.build(lookup, preorder, 0, len(preorder) - 1)
        
    def build(self, lookup, preorder, start, end):
        if not preorder:
            return
        node = TreeNode(preorder[0])
        mid = lookup[preorder[0]]
        node.left = self.build(lookup, preorder[1: 1 + mid - start], start, mid - 1)
        node.right = self.build(lookup, preorder[1 + mid - start: end + 1], mid + 1, end)
        return node

if __name__ == "__main__":
    root = Solution().buildTree([1, 2], [2, 1])
