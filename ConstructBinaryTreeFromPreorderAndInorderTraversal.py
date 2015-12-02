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
        return self.buildHelper(lookup, preorder, 0, 0, len(preorder))
        
    def buildHelper(self, lookup, pre, pre_start, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(pre[pre_start])
        i = lookup[pre[pre_start]]
        node.left = self.buildHelper(lookup, pre, pre_start + 1, in_start, i)
        node.right = self.buildHelper(lookup, pre, pre_start + i - in_start + 1, i + 1, in_end)
        return node

if __name__ == "__main__":
    root = Solution().buildTree([1, 2], [2, 1])
