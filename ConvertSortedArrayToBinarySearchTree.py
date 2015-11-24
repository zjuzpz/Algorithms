"""
108. Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(logn)
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        return self.recur(nums, 0, len(nums))
        
        
    def recur(self, nums, start, end):
        if start == end:
            return
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.recur(nums, start, mid)
        root.right = self.recur(nums, mid + 1, end)
        return root

    def traversal(self, res, root):
        if not root:
            return 
        self.traversal(res, root.left)
        res.append(root.val)
        self.traversal(res, root.right)

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    root = Solution().sortedArrayToBST(nums)
    res = []
    Solution().traversal(res, root)
    print(res)
    
