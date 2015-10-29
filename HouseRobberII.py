"""
213. House Robber II
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
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
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[0:len(nums) - 1]), self.robHelper(nums[1:]))
        
    def robHelper(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[-1], nums[-2])

if __name__ == "__main__":
    nums = [1,2,3,4,5,4,3,9,10]
    print(Solution().rob(nums))
