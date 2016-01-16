"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
# O(m * n)
# O(1)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        res = []
        top, right, bottom, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom):
                res.append(matrix[i][right])
            if bottom > top:
                for i in reversed(range(left, right + 1)):
                    res.append(matrix[bottom][i])
            if right > left:
                for i in reversed(range(top + 1, bottom)):
                    res.append(matrix[i][left])
            top, right, bottom, left = top + 1, right - 1, bottom - 1, left + 1
        return res

class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        times = (min(m, n) + 1) // 2
        i, res = 0, []
        while i < times:
            for j in range(i, n - i):
                res.append(matrix[i][j])
            for j in range(i + 1, m - i - 1):
                res.append(matrix[j][n - i - 1])
            if m - 1 - i != i:
                for j in reversed(range(i, n - i)):
                    res.append(matrix[m - i - 1][j])
            if n - 1 - i != i:
                for j in reversed(range(i + 1, m - i - 1)):
                    res.append(matrix[j][i])
            i += 1
        return res

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution2().spiralOrder(matrix))
