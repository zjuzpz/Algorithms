"""
289. Game of Life
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
# O(m * n)
# O(1)
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.nextTurn(board, i, j)
    #Refresh
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "c0" or board[i][j] == "c2":
                    board[i][j] = 0
                else:
                    board[i][j] = 1
                    
    def nextTurn(self, board, x, y):
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and (x != i or y != j):
                    if board[i][j] in (1, "c2", "c3"):
                        count += 1
        if board[x][y] == 0:
            if count == 3:
                board[x][y] = "c1"
            else:
                board[x][y] = "c0"
        else:
            if 2 <= count <= 3:
                board[x][y] = "c3"
            else:
                board[x][y] = "c2"

class Solution2(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] & 1 == 1:
                            count += 1
                if count == 3 or (count == 4 and board[i][j] == 1):
                    board[i][j] |= 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1

if __name__ == "__main__":
    board = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 0]]
    for i in range(5):
        Solution2().gameOfLife(board)
        print(board)
