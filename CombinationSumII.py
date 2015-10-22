"""
40. Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
"""
# O(k * C(n, k))
# O(k)

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.recur(candidates, target, [], res)
        return res
        
    def recur(self, c, target, cur, res):
        for i in range(len(c)):
            if c[i] < target:
                cur.append(c[i])
                self.recur(c[i + 1:], target - c[i], cur, res)
                cur.pop()
            elif c[i] == target:
                cur.append(c[i])
                if cur not in res:
                    res.append(cur[:])
                cur.pop()
                return
            else:
                return

if __name__ == "__main__":
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
