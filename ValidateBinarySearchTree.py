"""
98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(1)
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        previous = float("-inf")
        cur = root
        while cur:
            if not cur.left:
                if cur.val <= previous:
                    return False
                previous = cur.val
                cur = cur.right
            else:
                tem = cur.left
                while tem.right and tem.right != cur:
                    tem = tem.right
                if not tem.right:
                    tem.right = cur
                    cur = cur.left
                else:
                    if cur.val <= previous:
                        return False
                    previous = cur.val
                    cur = cur.right
                    tem.right = None
        return True

# O(n)
# O(h)
class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root, float("inf"), float("-inf"))
        
    def recur(self, root, high, low):
        if not root:
            return True
        return low < root.val < high and self.recur(root.left, root.val, low) \
               and self.recur(root.right, high, root.val)

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBST(root))
