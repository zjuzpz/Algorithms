"""
130. Surrounded Regions
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""
# O(m * n)
# O(m + n)

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        m, n, stack = len(board), len(board[0]), []
        for j in range(n):
            self.helper(board, 0, j, stack)
            self.helper(board, m - 1, j, stack)
        for i in range(m):
            self.helper(board, i, 0, stack)
            self.helper(board, i, n - 1, stack)
        while stack:
            (i, j) = stack.pop()
            self.helper(board, i - 1, j, stack)
            self.helper(board, i + 1, j, stack)
            self.helper(board, i, j - 1, stack)
            self.helper(board, i, j + 1, stack)
        for i in range(m):
            for j in range(n):
                if board[i][j] == True:
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                
    def helper(self, board, i, j, stack):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == "O":
            board[i][j] = True
            stack.append((i, j))

if __name__ == "__main__":
    board = [["O", "O"],["O","O"]]
    Solution().solve(board)
    print(board)
