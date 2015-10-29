"""
221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
# O(n * m)
# O(1)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if not matrix:
            return res
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                res = 1
                matrix[i][0] = 1
            else:
                matrix[i][0] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == "1":
                res = 1
                matrix[0][j] = 1
            else:
                matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                    res = max(res, matrix[i][j])
        return res * res


if __name__ == "__main__":
    matrix = [["1", "0", "1"],["1", "1", "1"],["1", "1", "1"]]
    print(Solution().maximalSquare(matrix))
