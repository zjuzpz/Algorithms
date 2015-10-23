"""
37. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
"""
class Solution(object):
    board = None
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solveSudokuHelper(self.board)
        board = self.board
        
    def solveSudokuHelper(self, board):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    k = 1
                    while k < 10:
                        self.board[i][j] = str(k)
                        if self.isValid(self.board, i, j) and self.solveSudokuHelper(self.board):
                            return True
                        else:
                            k += 1
                    self.board[i][j] = "."
                    return False
        return True
    
    def isValid(self, board, x, y):
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            for j in range(y // 3 * 3, y // 3 * 3 + 3):
                if (i, j) != (x, y) and board[i][j] == board[x][y]:
                    return False
        return True

if __name__ == "__main__":
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    Solution().solveSudoku(board)
    print(board)
