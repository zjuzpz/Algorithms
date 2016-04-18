"""
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element

and your function should return the index number 2.
"""
# O(logn)
# O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if mid == 0:
                if len(nums) == 1 or nums[mid] > nums[mid + 1]:
                    return mid
                return mid + 1
            if nums[mid] > nums[mid - 1]:
                if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                    return mid
                lower = mid + 1
            else:
                upper = mid - 1
        return lower

if __name__ == "__main__":
    print(Solution().findPeakElement([1,2,3,1]))
