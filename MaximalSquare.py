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
# O(m * n)
# O(m * n)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        a = 0
        res = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                res[i][0] = 1
                a = 1
        for j in range(len(matrix[0])):
            if matrix[0][j] == "1":
                res[0][j] = 1
                a = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    res[i][j] = min(res[i - 1][j], res[i][j - 1], res[i - 1][j - 1]) + 1
                    a = max(a, res[i][j])
        return a ** 2


if __name__ == "__main__":
    matrix = [["1", "0", "1"],["1", "1", "1"],["1", "1", "1"]]
    print(Solution().maximalSquare(matrix))
