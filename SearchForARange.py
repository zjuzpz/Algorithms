"""
34. Search for a Range
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
# O(logn)
# O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] < target:
                lower += 1
            else:
                upper -= 1
        if nums[upper] == target:
            left = upper
        elif upper + 1 < len(nums) and nums[upper + 1] == target:
            left = upper + 1
        else:
            return [-1, -1]
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] > target:
                upper -= 1
            else:
                lower += 1
        if nums[lower] == target:
            right = lower
        elif lower - 1 >= 0 and nums[lower - 1] == target:
            right = lower - 1
        return [left, right]

if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))
