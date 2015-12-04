"""
152. Maximum Product Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
# O(n)
# O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_min, local_max, global_max = 1, 1, float("-inf")
        for num in nums:
            local_min, local_max = min(local_min * num, local_max * num, num), max(local_min * num, local_max * num, num)
            global_max = max(global_max, local_max)
        return global_max

if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))
