"""
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == i:
                i += 1
            elif nums[i] > j:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                tem = nums[i]
                nums[i], nums[tem] = nums[tem], nums[i]
        if nums[j] == j:
            return j + 1
        return j

class Solution3(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i + 1
        return res

import functools
import operator
class Solution4(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return functools.reduce(operator.xor, nums, \
                      functools.reduce(operator.xor, range(len(nums) + 1)))

if __name__ == "__main__":
    print(Solution3().missingNumber([1]))
