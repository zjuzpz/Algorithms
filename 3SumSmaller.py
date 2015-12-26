"""
259. 3Sum Smaller
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
"""
# O(n ^ 2)
# O(1)
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i, res = 0, 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    res += k - j
                    j += 1
                else:
                    k -= 1
            i += 1
        return res

if __name__ == "__main__":
    nums = [3, 1, -2, 0]
    target = 2
    print(Solution().threeSumSmaller(nums, target))
