"""
307. Range Sum Query - Mutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""
# O(n) for init O(logn) for update and sum
# O(n)
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # Build binary indexed tree
        self.__bit = [0 for i in range(len(nums) + 1)]
        self.__nums = nums
        for i in range(len(nums)):
            self.__add(i, nums[i])
            
    def __add(self, i, val):
        i += 1
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if val != self.__nums[i]:
            self.__add(i, val - self.__nums[i])
            self.__nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def helper(i):
            i += 1
            res = 0
            while i > 0:
                res += self.__bit[i]
                i -= (i & -i)
            return res
        
        res = helper(j)
        if i > 0:
            res -= helper(i - 1)
        return res

if __name__ == "__main__":
    nums = [1, 3, 5]
    n = NumArray(nums)
    print(n.sumRange(0, 2))
    n.update(1, 2)
    n.sumRange(0, 2)
