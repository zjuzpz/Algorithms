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
        if len(nums) <= 3:
            return []
        nums.sort()
        lookup, visited = {}, set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                tem = nums[i] + nums[j]
                if tem not in lookup:
                    lookup[tem] = [[i, j]]
                    visited.add((nums[i], nums[j]))
                elif (nums[i], nums[j]) not in visited:
                    lookup[tem].append([i, j])
                    visited.add((nums[i], nums[j]))
        res, visited = [], set()
        for c in range(2, len(nums) - 1):
            for d in range(c + 1, len(nums)):
                tem = target - nums[c] - nums[d]
                if tem in lookup:
                    for [a, b] in lookup[tem]:
                        if b < c:
                            candidate = [nums[a], nums[b], nums[c], nums[d]]
                            key = "".join(str(candidate))
                            if key not in visited:
                                visited.add(key)
                                res.append(candidate)
        return res

class Solution2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums, result, lookup = sorted(nums), [], {}
        i = 0
        while i < len(nums) - 1:
            while i != 0 and nums[i] == nums[i - 1]:
                i += 1
                if i >= len(nums) - 1:
                    break
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] not in lookup:
                    lookup[nums[i] + nums[j]] = [[i, j]]
                else:
                    lookup[nums[i] + nums[j]].append([i, j])
                j += 1
                while j < len(nums) and j != 1 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
        for c in range(2, len(nums)):
            for d in range(c+1, len(nums)):
                if target - nums[c] - nums[d] in lookup:
                    for [a, b] in lookup[target - nums[c] - nums[d]]:
                        if b < c:
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            if quad not in result:
                                result.append(quad)
        return result

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(Solution().fourSum(nums, target))
