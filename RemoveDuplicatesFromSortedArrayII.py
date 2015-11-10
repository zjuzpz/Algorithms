"""
80. Remove Duplicates from Sorted Array II
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""
# O(n)
# O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        visited, index = False, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if not visited:
                    visited = True
                    nums[index] = nums[i]
                    index += 1
            else:
                visited = False
                nums[index] = nums[i]
                index += 1
        return index

if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,1,1,2,2,2,3,4,5]))
