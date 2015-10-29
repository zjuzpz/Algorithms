"""
217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""
# O(n)
# O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = {}
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited[nums[i]] = True
            else:
                return True
        return False

if __name__ == "__main__":
    print(Solution().containsDuplicate([1,4,3,2,5,6,2]))
