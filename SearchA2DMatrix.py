"""
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
# O(logm + logn)
# O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        
        # find row
        lower, upper = 0, m - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                upper = mid - 1
            else:
                lower = mid + 1
        if matrix[lower][0] == target:
            return True
        if matrix[lower][0] > target:
            if lower == 0:
                return False
            index = lower - 1
        else:
            index = lower
            
        # find colunm
        lower, upper = 0, n - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if matrix[index][mid] == target:
                return True
            if matrix[index][mid] > target:
                upper = mid - 1
            else:
                lower = mid + 1
        if matrix[index][lower] == target:
            return True
        return False

class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        lower, upper = 0, m * n - 1
        while lower < upper:
            mid = (lower + upper) // 2
            num = matrix[mid // n][mid % n]
            if num == target:
                return True
            if num > target:
                upper = mid - 1
            else:
                lower = mid + 1
        if matrix[lower // n][lower % n] == target:
            return True
        return False

if __name__ == "__main__":
    matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    print(Solution().searchMatrix(matrix, 11))
