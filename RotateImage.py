"""
48. Rotate image
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
"""
# Time:  O(n^2)
# Space: O(1)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        times, i, j = len(matrix) // 2, 0, len(matrix) - 1
#rotate times
        while times > 0:
            matrix = self.rot(matrix, i, j)
            times, i, j = times - 1, i + 1, j - 1
        return
    
    def rot(self, matrix, i, j):
        for k in range(i, j):
            matrix[i][k], matrix[k][j], \
            matrix[j][len(matrix) - k - 1], matrix[len(matrix) - k - 1][i] = \
            matrix[len(matrix) - k - 1][i], matrix[i][k], \
            matrix[k][j], matrix[j][len(matrix) - k - 1]
        return matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3], [5, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(matrix)
