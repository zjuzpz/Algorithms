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
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] > target:
                upper = mid - 1
            elif nums[mid] < target:
                lower = mid + 1
            else:
                upper = mid
        if nums[lower] != target:
            return [-1, -1]
        left = lower
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] > target:
                upper = mid - 1
            elif nums[mid] < target:
                lower = mid + 1
            else:
                lower = mid + 1
        if lower > 0 and nums[lower] != target:
            right = lower - 1
        else:
            right = lower
        return [left, right]


if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))
