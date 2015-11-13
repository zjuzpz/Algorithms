"""
114. Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""
# O(n)
# O(n)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        res, cur = [], root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                tem = cur.left
                while tem.right and tem.right != cur:
                    tem = tem.right
                if not tem.right:
                    tem.right = cur
                    res.append(cur.val)
                    cur = cur.left
                else:
                    cur = cur.right
                    tem.right = None
        root.left = None
        for i in range(1, len(res)):
            root.right = TreeNode(res[i])
            root = root.right

# O(n)
# O(h)
class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            tem = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = tem

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    Solution().flatten(root)
    while root:
        print(root.val)
        root = root.right
