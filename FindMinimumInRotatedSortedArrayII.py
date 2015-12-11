"""
154. Find Minimum in Rotated Sorted Array II
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
# O(logn ~ n)
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
            if nums[upper] > nums[lower]:
                return nums[lower]
            elif nums[upper] < nums[lower]:
                if nums[mid] >= nums[lower]:
                    lower = mid + 1
                else:
                    upper = mid
            else:
                lower += 1
        return nums[lower]

if __name__ == "__main__":
    print(Solution().findMin([3, 1, 1, 2, 2, 3]))
