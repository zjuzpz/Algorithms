"""
222. Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(logn ^ 2)
# O(1)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        h = self.cal_height(root)
        lower, upper = 2 ** (h - 1), 2 ** h - 1
        cur = root
        while lower < upper:
            mid = (lower + upper) // 2
            if self.cal_height(cur.right) == h - 1:
                lower = mid + 1
                cur = cur.right
            else:
                upper = mid
                cur = cur.left
            h -= 1
        return lower
        
    def cal_height(self, root):
        cur, h = root, 0
        while cur:
            h += 1
            cur = cur.left
        return h

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    print(Solution().countNodes(root))
