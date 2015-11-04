"""
41. First Missing Positive
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


"""
A very tricky bug:
Assume l = [1,0]
We can use l[0], l[1] = l[1], l[0]
But we cannnot use l[0], l[l[0]] = l[l[0]], l[0]
"""
# O(n)
# O(1)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == i + 1:
                i += 1
            elif nums[i] < i + 1 or nums[i] > j + 1 or nums[nums[i] - 1] == nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                position = nums[i] - 1
                nums[i], nums[position] = nums[position], nums[i]
        if nums[i] == i + 1:
            return i + 2
        return i + 1
        

if __name__ == "__main__":
    nums = [2,1]
    print(Solution().firstMissingPositive(nums))
