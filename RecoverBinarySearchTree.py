"""
99. Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(1)
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cur = root
        node1, node2, node_prev, node_cur = None, None, None, None
        while cur:
            if not cur.left:
                node_cur = cur
                cur = cur.right
            else:
                tem = cur.left
                while tem.right and tem.right != cur:
                    tem = tem.right
                if not tem.right:
                    tem.right = cur
                    cur = cur.left
                else:
                    node_cur = cur
                    cur = cur.right
                    tem.right = None
            if node_prev and node_prev.val > node_cur.val:
                if not node1:
                    node1, node2 = node_prev, node_cur
                else:
                    node2 = node_cur
            node_prev = node_cur
        node1.val, node2.val = node2.val, node1.val

if __name__ == "__main__":
    root = TreeNode(3)
    root.right = TreeNode(1)
    root.right.left = TreeNode(2)
    Solution().recoverTree(root)
