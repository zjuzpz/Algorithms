"""
73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
# O(m * n)
# O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.setX(matrix, i, j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "X":
                    matrix[i][j] = 0
                    
    def setX(self, matrix, x, y):
        matrix[x][y] = "X"
        for i in range(len(matrix)):
            if matrix[i][y] != 0:
                matrix[i][y] = "X"
        for j in range(len(matrix[0])):
            if matrix[x][j] != 0:
                matrix[x][j] = "X"

if __name__ == "__main__":
    matrix = [[1,1,1], [2,0,2], [9,8,7]]
    Solution().setZeroes(matrix)
    print(matrix)
