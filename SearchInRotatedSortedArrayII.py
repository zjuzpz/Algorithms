"""
81. Search in Rotated Sorted Array II
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""
# O(logn)
# O(1)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[lower]:
                if  nums[lower] <= target < nums[mid]:
                    upper = mid - 1
                else:
                    lower = mid + 1
            elif nums[mid] < nums[lower]:
                if nums[mid] < target <= nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid - 1
            else:
                lower += 1
        return nums[lower] == target

if __name__ == "__main__":
    print(Solution().search([1,3,1,1,1], 3))
