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
        return res

class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        jump, last, cur = 0, 0, nums[0]
        while last < len(nums) - 1:
            jump += 1
            next_turn = 0
            max_reach = min(len(nums) - 1, cur)
            for i in range(last + 1, max_reach + 1):
                next_turn = max(next_turn, i + nums[i])
            last = max_reach
            cur = next_turn
        return jump
    
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution2().jump(nums))
