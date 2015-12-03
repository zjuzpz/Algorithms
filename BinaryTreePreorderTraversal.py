"""
144. Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
 Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3



return [1,2,3]. 
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# O(n)
# O(1)
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
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
        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().preorderTraversal(root))
