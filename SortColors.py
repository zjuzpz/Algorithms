"""
75. Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note:
You are not suppose to use the library's sort function for this problem.
"""
# O(n)
# O(1)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, cur = 0, len(nums) - 1, 0
        while cur <= j:
            if nums[cur] == 0:
                nums[cur], nums[i] = nums[i], nums[cur]
                i += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[j] = nums[j], nums[cur]
                j -= 1
            if cur < i:
                cur += 1

if __name__ == "__main__":
    nums = [2,2,1,0,1,2,0]
    Solution().sortColors(nums)
    print(nums)
