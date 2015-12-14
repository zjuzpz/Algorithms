"""
215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
# O(n)
# O(1)
from random import randint
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            pivot_idx = randint(start, end)
            new_pivot_idx = self.partition(nums, pivot_idx, start, end)
            if new_pivot_idx == len(nums) - k:
                return nums[new_pivot_idx]
            if new_pivot_idx > len(nums) - k:
                end = new_pivot_idx - 1
            else:
                start = new_pivot_idx + 1
                
    def partition(self, nums, idx, start, end):
        pivot_val = nums[idx]
        nums[idx], nums[end] = nums[end], nums[idx]
        new_pivot_idx = start
        for i in range(start, end):
            if nums[i] < pivot_val:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1
        nums[new_pivot_idx], nums[end] = nums[end], nums[new_pivot_idx]
        return new_pivot_idx

if __name__ == "__main__":
    nums = [8, 4, 1, 0, 4, 2, 9, 11, 99, 3, 2]
    print(Solution().findKthLargest(nums, 3))
