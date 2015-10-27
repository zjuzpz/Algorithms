"""
36. Valid Sudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not self.check(board, i, j):
                        return False
        return True
        
    def check(self, board, x, y):
        for i in range(x + 1, 9):
            if board[i][y] == board[x][y]:
                return False
        for j in range(y + 1, 9):
            if board[x][j] == board[x][y]:
                return False
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            for j in range(y // 3 * 3, y // 3 * 3 + 3):
                if (i, j) != (x, y) and board[i][j] == board[x][y]:
                    return False
        return True

if __name__ == "__main__":
    board = [['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],\
             ['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],\
             ['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],\
             ['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],\
             ['.','.','.','.','8','.','.','7','9']]
    print(Solution().isValidSudoku(board))
    
