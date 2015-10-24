"""
45. Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
# O(n)
# O(1)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        res, prev, cur = 0, 0, 0
        for i in range(len(nums)):
            cur = max(cur, i + nums[i])
            if cur >= len(nums) - 1:
                return res + 1
            if i == prev:
                res += 1
                prev = cur

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution2().jump(nums))
