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
        root = self.build(lookup, preorder, 0, len(preorder) - 1)
        return root
        
    def build(self, lookup, pre, in_start, in_end):
        if not pre:
            return
        node = TreeNode(pre[0])
        mid = lookup[pre[0]]
        length_left = mid - in_start
        node.left = self.build(lookup, pre[1: 1 + length_left], in_start, mid - 1)
        node.right = self.build(lookup, pre[1 + length_left: in_end + 1], mid + 1, in_end)
        return node

if __name__ == "__main__":
    root = Solution().buildTree([1, 2], [2, 1])
