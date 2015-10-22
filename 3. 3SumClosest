"""
16. 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""
# O(n^2)
# O(1)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = float("inf")
        nums.sort();
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                tem = nums[i] + nums[j] + nums[k]
                if tem == target:
                    return target
                if tem > target:
                    if abs(res) > tem - target:
                        res = tem - target
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    if abs(res) > target - tem:
                        res = tem - target
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res + target

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 2
    print(Solution().threeSumClosest(nums, target))
