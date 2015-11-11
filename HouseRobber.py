"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
# O(n)
# O(1)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        num1, num2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            num2, num1 = max(nums[i] + num1, num2), num2
        return max(num1, num2)

if __name__ == "__main__":
    print(Solution().rob([1,2,3,1,2,2]))
