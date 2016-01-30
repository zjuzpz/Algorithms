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
        return self.build(lookup, postorder, 0, len(inorder) - 1)
        
    def build(self, lookup, post, in_start, in_end):
        if not post:
            return
        node = TreeNode(post[-1])
        mid = lookup[post[-1]]
        length_left, length_right = mid - in_start, in_end - mid
        node.left = self.build(lookup, post[0 : length_left], in_start, mid - 1)
        node.right = self.build(lookup, post[-1 - length_right : -1], mid + 1, in_end)
        return node

if __name__ == "__main__":
    root = Solution().buildTree([1, 2], [2, 1])
    print(root.val, root.right.val)
