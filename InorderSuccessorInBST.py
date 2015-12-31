"""
285. Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(h)
# O(1)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur = p.right
        if cur:
            while cur.left:
                cur = cur.left
            return cur
        cur, res = root, None
        while cur:
            if cur.val > p.val:
                res = cur
                cur = cur.left
            else:
                cur = cur.right
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.right = TreeNode(4)
    print(Solution().inorderSuccessor(root, root.left.left).val)
