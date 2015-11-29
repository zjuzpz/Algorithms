"""
59. Spiral Matrix II
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
# O(n ^ 2)
# O(1)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        res = [[False for j in range(n)] for i in range(n)]
        times = n // 2
        times += n % 2
        num, k = 1, 0
        while k < times:
            for j in range(k, n - k):
                res[k][j] = num
                num += 1
            for i in range(k + 1, n - 1 - k):
                if not res[i][n - 1 - k]:
                    res[i][n - 1 - k] = num
                    num += 1
            for j in reversed(range(k, n - k)):
                if not res[n - 1 - k][j]:
                    res[n - 1 - k][j] = num
                    num += 1
            for i in reversed(range(k + 1, n - 1 - k)):
                if not res[i][k]:
                    res[i][k] = num
                    num += 1
            k += 1
        return res

if __name__ == "__main__":
    print(Solution().generateMatrix(3))
