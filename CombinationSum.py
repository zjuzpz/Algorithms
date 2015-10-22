"""
39. Combination Sum
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
"""
# O(k * n^k)
# O(k)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.recur(candidates, target, [], res)
        return res
        
    def recur(self, nums, target, cur, res):
        for i in range(len(nums)):
            cur.append(nums[i])
            if nums[i] == target:
                res.append(cur[:])
                cur.pop()
                break
            elif nums[i] > target:
                cur.pop()
                break
            else:
                self.recur(nums[i:], target - nums[i], cur, res)
                cur.pop()

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))
