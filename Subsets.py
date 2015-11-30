"""
78. Subsets
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
# O(n * 2 ^ n)
# O(1)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        self.recur(res, nums, 0, len(nums), [])
        return res
        
    def recur(self, res, nums, start, end, cur):
        if start == end:
            return
        for i in range(start, end):
            cur.append(nums[i])
            res.append(cur[:])
            self.recur(res, nums, i + 1, end, cur)
            cur.pop()

if __name__ == "__main__":
    print(Solution().subsets([3,6,4,1,9,0]))
