"""
272. Closest Binary Search Tree Value II
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(k)
from collections import deque
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res, cur = deque(), root
        while cur:
            if not cur.left:
                if len(res) < k:
                    res.append(cur.val)
                elif abs(cur.val - target) < abs(res[0] - target):
                    res.popleft()
                    res.append(cur.val)
                else:
                    break
                cur = cur.right
            else:
                tem = cur.left
                while tem.right and tem.right != cur:
                    tem = tem.right
                if not tem.right:
                    tem.right = cur
                    cur = cur.left
                else:
                    if len(res) < k:
                        res.append(cur.val)
                    elif abs(cur.val - target) < abs(res[0] - target):
                        res.popleft()
                        res.append(cur.val)
                    else:
                        tem.right = None
                        break
                    cur = cur.right
                    tem.right = None
        return list(res)

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    print(Solution().closestKValues(root, 3.5, 3))
