"""
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
# O(n!)
# O(n)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 or n < k:
            return []
        res = []
        self.recur(res, 1, n, k, [])
        return res
    
    def recur(self, res, start, n, k, cur):
        if k == 0:
            res.append(cur[:])
            return
        if n - start + 1 < k:
            return
        for i in range(start, n + 1):
            cur.append(i)
            self.recur(res, i + 1, n, k - 1, cur)
            cur.pop()

if __name__ == "__main__":
    print(Solution().combine(4,2))
