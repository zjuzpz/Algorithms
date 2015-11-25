"""
95. Unique Binary Search Trees II
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        return self.recur(1, n + 1)
        
    def recur(self, start, end):
        if start == end:
            return [None]
        res = []
        for i in range(start, end):
            left = self.recur(start, i)
            right = self.recur(i + 1, end)
            for j in left:
                for k in right:
                    root = TreeNode(i)
                    root.left = j
                    root.right = k
                    res.append(root)
        return res


if __name__ == "__main__":
    print(Solution().generateTrees(0))
