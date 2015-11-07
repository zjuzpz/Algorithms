"""
51. N-Queens
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
# O(n!)
# O(n)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        i, res, board = 0, [], [["." for j in range(n)] for i in range(n)]
        self.recur(res, i, board, n)
        return res
        
    def recur(self, res, i, board, n):
        if i >= n:
            res.append(["".join(board[i]) for i in range(n)])
            return
        for j in range(n):
            board[i][j] = "Q"
            if self.isValid(board, i, j, n):
                self.recur(res, i + 1, board, n)
            board[i][j] = "."
            
    def isValid(self, board, x, y, n):
        for i in range(x):
            if board[i][y] == "Q":
                return False
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i, j = i - 1, j - 1
        i, j = x - 1, y + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i, j = i - 1, j + 1
        return True

if __name__ == "__main__":
    print(Solution().solveNQueens(4))
