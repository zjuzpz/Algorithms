"""
207. Kth Smallest Element in a BST 
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(k)
# O(1)
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cur = root
        while cur:
            if not cur.left:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
            else:
                tem = cur.left
                while tem.right and tem.right != cur:
                    tem = tem.right
                if not tem.right:
                    tem.right = cur
                    cur = cur.left
                else:
                    k -= 1
                    if k == 0:
                        return cur.val
                    tem.right = None
                    cur = cur.right

# O(max(k, h))
# O(h)
class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        cur = root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().kthSmallest(root, 4))
