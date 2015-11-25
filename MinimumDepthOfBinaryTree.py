"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(n)
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cur = [root]
        depth = 1
        while cur:
            tem = []
            for node in cur:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    tem.append(node.left)
                if node.right:
                    tem.append(node.right)
            depth += 1
            cur = tem

# O(n)
# O(h)
class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.recur(1, root)
        
    def recur(self, depth, root):
        if not root.left and not root.right:
            return depth
        if root.left and root.right:
            return min(self.recur(depth + 1, root.left), self.recur(depth + 1, root.right))
        if root.left:
            return self.recur(depth + 1, root.left)
        return self.recur(depth + 1, root.right)

class Solution3(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution3().minDepth(root))
