"""
329. Longest Increasing Path in a Matrix
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
# O(m * n)
# O(m * n)
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        path, res = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))], 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not path[i][j]:
                    res = max(res, self.DFS(path, matrix, i, j))
        return res
        
    def DFS(self, path, matrix, i, j):
        if path[i][j]:
            return path[i][j]
        temMax = 0
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if matrix[x][y] > matrix[i][j]:
                    temMax = max(temMax, self.DFS(path, matrix, x, y))
        path[i][j] = temMax + 1
        return path[i][j]

if __name__ == "__main__":
    m = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    print(Solution().longestIncreasingPath(m))
