"""
103. Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(n)
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, cur, reverse = [[root.val]], [root], True
        while cur:
            tem, val = [], []
            for node in cur:
                if node.left:
                    tem.append(node.left)
                    val.append(node.left.val)
                if node.right:
                    tem.append(node.right)
                    val.append(node.right.val)
            if val != []:
                if reverse:
                    val.reverse()
                    res.append(val)
                    reverse = False
                else:
                    res.append(val)
                    reverse = True
            cur = tem
        return res

if __name__ == "__main__":
    root =TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))
