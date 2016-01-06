"""
280. Wiggle Sort
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""
# O(n)
# O(1)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag = True
        for i in range(1, len(nums)):
            if flag and nums[i] < nums[i - 1]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
            elif not flag and nums[i] > nums[i - 1]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
            flag = not flag

if __name__ == "__main__":
    nums = [3, 5, 2, 1, 6, 4]
    Solution().wiggleSort(nums)
    print(nums)
