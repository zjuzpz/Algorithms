"""
37. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
"""
# O((9!) ^ 9)
# O(1)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solveSudokuHelper(board)
        
    def solveSudokuHelper(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        board[i][j] = str(k)
                        if self.isValid(board, i, j) and self.solveSudokuHelper(board):
                            return True
                    board[i][j] = "."
                    return False
        return True
    
    def isValid(self, board, x, y):
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
            if i != y and board[x][i] == board[x][y]:
                return False
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            for j in range(y // 3 * 3, y // 3 * 3 + 3):
                if (i, j) != (x, y) and board[i][j] == board[x][y]:
                    return False
        return True

class Solution2(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        stack = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    stack.append((i, j))
        self.recur(board, stack)
        
    def recur(self, board, stack):
        if not stack:
            return True
        (x, y) = stack.pop()
        for i in range(1, 10):
            board[x][y] = str(i)
            if self.isValid(board, x, y) and self.recur(board, stack):
                return True
        board[x][y] = "."
        stack.append((x, y))
        return False
    
    def isValid(self, board, x, y):
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
            if i != y and board[x][i] == board[x][y]:
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
