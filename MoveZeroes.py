"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
# O(n)
# O(1)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, cur, j = 0, 0, len(nums) - 1
        while cur < len(nums):
            if nums[cur] == 0:
                j -= 1
            else:
                nums[i] = nums[cur]
                i += 1
            cur += 1
        j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
