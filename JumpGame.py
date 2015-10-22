"""
55. Jump game
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
# O(n)
# O(1)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            if nums[i] > 0:
                reach = max(reach, i + nums[i])
        return True

if __name__ == "__main__":
    print(Solution().canJump([3,2,1,0,4]))
