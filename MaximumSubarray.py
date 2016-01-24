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

# O(nlogn)
# O(logn)
class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.divide(0, len(nums) - 1, nums)
        
    def divide(self, start, end, nums):
        if start == end:
            return nums[start]
        mid = (start + end) // 2
        left = self.divide(start, mid, nums)
        right = self.divide(mid + 1, end, nums)
        maxLeftContSum = nums[mid]
        localMaxSum = nums[mid]
        for i in reversed(range(0, mid)):
            localMaxSum += nums[i]
            maxLeftContSum = max(maxLeftContSum, localMaxSum)
        maxRightContSum = nums[mid + 1]
        localMaxSum = nums[mid + 1]
        for i in range(mid + 2, end + 1):
            localMaxSum += nums[i]
            maxRightContSum = max(maxRightContSum, localMaxSum)
        return max(left, right, maxLeftContSum + maxRightContSum)
if __name__ == "__main__":
    nums = [-2,1,-3,4-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))
