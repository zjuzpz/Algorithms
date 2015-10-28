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
        sum = 0
        i, start = 0, 0
        while i < len(nums):
            sum += nums[i]
            while sum >= s:
                res = min(res, i - start + 1)
                sum -= nums[start]
                start += 1
            i += 1
        if res == float("inf"):
            return 0
        return res

if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
