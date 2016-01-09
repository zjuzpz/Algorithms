"""
279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
# O(n ^ 1.5)
# O(n)
class Solution(object):
    _res = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = self._res
        while len(res) <= n:
            t = set()
            for i in range(1, int(len(res) ** 0.5) + 1):
                t.add(res[- i * i] + 1)
            res.append(min(t))
        return res[n]
    
if __name__ == "__main__":
    print(Solution().numSquares(1024))

