"""
90. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
# O(n * 2 ^ n)
# O(n)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.recur(res, nums, [])
        return res
        
    def recur(self, res, nums, cur):
        res.append(cur[:])
        i = 0
        while i < len(nums):
            cur.append(nums[i])
            self.recur(res, nums[i + 1:], cur)
            cur.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1


if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,2,2])
