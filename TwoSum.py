"""
1. Two Sum
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i in range(len(nums)):
            if target - nums[i] in lookup:
                return [lookup[target - nums[i]] + 1, i + 1]
            lookup[nums[i]] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
