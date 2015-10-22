"""
15. 3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
"""
# O(n^2)
# O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            target = 0 - nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    candidate = [nums[i], nums[start], nums[end]]
                    if candidate not in res:
                        res.append(candidate)
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                else:
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return res

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, 4]
    print(Solution().threeSum(nums))
