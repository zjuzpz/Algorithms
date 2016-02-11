"""
209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
# O(n)
# O(1)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf")
        i, j, sum = 0, 0, 0
        while j < len(nums):
            sum += nums[j]
            while i <= j and sum >= s:
                res = min(res, j - i + 1)
                sum -= nums[i]
                i += 1
            j += 1
        return 0 if res == float("inf") else res

# O(nlogn)
# O(n)
class Solution2(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = float("inf")
        sum = [nums[0]]
        for i in range(1, len(nums)):
            sum.append(sum[-1] + nums[i])
        if sum[-1] < s:
            return 0
        j = len(sum) - 1
        while j >= 0 and sum[j] >= s:
            target = sum[j] - s
            i = self.binarySearch(sum, target)
            res = min(res, j - i)
            j -= 1
        return res
        
    def binarySearch(self, nums, target):
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                upper = mid - 1
            else:
                lower = mid + 1
        if nums[lower] <= target:
            return lower
        return lower - 1

if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
