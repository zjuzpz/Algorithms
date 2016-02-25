"""
18. Four Sum
Given an array S of n integers, are there elements a, b, c, and d in S such that
a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""
# k * n ^ 2
# n ^ 2
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        lookup, res, visited = {}, [], set()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s not in lookup:
                    lookup[s] = set()
                lookup[s].add((i, j))
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                s = nums[a] + nums[b]
                if target - s in lookup:
                    for (c, d) in lookup[target - s]:
                        if c > b and (nums[a], nums[b], nums[c], nums[d]) not in visited:
                            res.append([nums[a], nums[b], nums[c], nums[d]])
                            visited.add((nums[a], nums[b], nums[c], nums[d]))
        return res

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(Solution().fourSum(nums, target))
