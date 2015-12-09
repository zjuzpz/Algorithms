"""
52. N-Queens II
Follow up for N-Queens problem.

Now, instead outputting board configurations,
return the total number of distinct solutions.
"""
# O(n!)
# O(n)
class Solution(object):
    res = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        board = [["." for j in range(n)] for i in range(n)]
        self.recur(board, n, 0)
        return self.res
        
    def recur(self, board, n, row):
        if row >= n:
            self.res += 1
            return
        for i in range(n):
            board[row][i] = "Q"
            if self.isValid(board, row, i):
                self.recur(board, n, row + 1)
            board[row][i] = "."
            
    def isValid(self, board, x, y):
        for i in range(x):
            if board[i][y] == "Q":
                return False
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i, j = i - 1, j - 1
        i, j = x - 1, y + 1
        while i >= 0 and j < len(board):
            if board[i][j] == "Q":
                return False
            i, j = i - 1, j + 1
        return True

if __name__ == "__main__":
    print(Solution().totalNQueens(8))
