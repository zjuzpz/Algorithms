"""
315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""
# O(n ^ 2)
# O(n)
from collections import deque
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = deque()
        res.appendleft(0)
        l = [nums[-1]]
        for i in reversed(range(len(nums) - 1)):
            index = self.insert(l, nums[i])
            res.appendleft(index)
            l.insert(index, nums[i])
        return list(res)
        
    def insert(self, nums, num):
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] >= num:
                upper = mid - 1
            else:
                lower = mid + 1
        return lower if nums[lower] >= num else lower + 1

# BIT
# O(nlogn)
# O(n)
class BIT(object):
    def __init__(self, n):
        self.__bit = [0 for i in range(n)]
        
    def add(self, i, val):
        while 0 < i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)
            
    def query(self, i):
        res = 0
        while i > 0:
            res += self.__bit[i]
            i -= (i & -i)
        return res

class Solution2(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_num, res = sorted(nums), [0 for i in range(len(nums))]
        bit = BIT(len(nums) + 1)
        for i in reversed(range(len(nums))):
            index = self.binarySearch(sorted_num, nums[i])
            res[i] = bit.query(index)
            bit.add(index + 1, 1)
        return res
        
    def binarySearch(self, nums, num):
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] >= num:
                upper = mid - 1
            else:
                lower = mid + 1
        return lower if nums[lower] == num else lower + 1

# BST
# O(nlogn)
# O(n)
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        #Count the numbers of left children
        self.count = 0
        
class BST(object):
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        node = TreeNode(val)
        if not self.root:
            self.root = node
            return
        cur = self.root
        while cur:
            if val < cur.val:
                cur.count += 1
                if not cur.left:
                    cur.left = node
                    break
                else:
                    cur = cur.left
            else:
                if not cur.right:
                    cur.right = node
                    break
                else:
                    cur = cur.right
                    
    def query(self, val):
        count = 0
        cur = self.root
        while cur:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                count += 1 + cur.count
                cur = cur.right
            else:
                return count + cur.count
        return 0
        
class Solution3(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(len(nums))]
        bst = BST()
        for i in reversed(range(len(nums))):
            bst.insert(nums[i])
            res[i] = bst.query(nums[i])
        return res

if __name__ == "__main__":
    nums = [5, 2, 6, 1]
    print(Solution3().countSmaller(nums))
