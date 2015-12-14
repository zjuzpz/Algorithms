"""
145. Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(1)
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dummy = TreeNode(-1)
        dummy.left = root
        res, cur = [], dummy
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                tem = cur.left
                tem_val = [tem.val]
                while tem.right and tem.right != cur:
                    tem = tem.right
                    tem_val.append(tem.val)
                if not tem.right:
                    tem.right = cur
                    cur = cur.left
                else:
                    while tem_val:
                        res.append(tem_val.pop())
                    cur = cur.right
                    tem.right = None
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print(Solution().postorderTraversal(root))
