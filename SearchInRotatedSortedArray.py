"""
33. Search in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
"""
# O(logn)
# O(1)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the pivot
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[upper] < nums[mid]:
                lower = mid + 1
            else:
                upper = mid
        minindex = upper
        lower, upper = 0, minindex - 1
        n1 = self.binarySearch(nums, lower, upper, target)
        if n1 != -1:
            return n1
        lower, upper = minindex, len(nums) - 1
        return self.binarySearch(nums, lower, upper, target)
        
    def binarySearch(self, nums, lower, upper, target):
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                upper = mid - 1
            else:
                lower = mid + 1
        if nums[lower] == target:
            return lower
        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    print(Solution().search(nums, 5))
