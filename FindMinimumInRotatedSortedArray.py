"""
153. Find Minimum in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
# O(logn)
# O(1)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[lower] < nums[upper]:
                return nums[lower]
            else:
                if nums[mid] < nums[upper]:
                    upper = mid
                else:
                    lower = mid + 1
        return nums[lower]

if __name__ == "__main__":
    print(Solution().findMin([2, 1]))
