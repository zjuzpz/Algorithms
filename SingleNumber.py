"""
136. Single Number
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""
# O(n)
# O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res

if __name__ == "__main__":
    print(Solution().singleNumber([1,3,2,4,5,2,3,1,5]))
