"""
53. Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
# O(n)
# O(1)
# For divide and conquer: O(nlogn)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max, global_max = float("-inf"), float("-inf")
        for i in range(len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            global_max = max(global_max, local_max)
        return global_max

if __name__ == "__main__":
    nums = [-2,1,-3,4-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))
