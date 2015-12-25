"""
303. Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
# O(n), O(1)
# O(n)
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if nums:
            self.nums = [nums[0]]
            for i in range(1, len(nums)):
                self.nums.append(self.nums[-1] + nums[i])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]

if __name__ == "__main__":
    l = NumArray([-2, 0, 3, -5, 2, -1])
    print(l.sumRange(0, 2))
    print(l.sumRange(2, 5))
    print(l.sumRange(0, 5))
