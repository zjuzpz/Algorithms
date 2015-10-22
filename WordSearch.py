"""
79. Word Search
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
# Time:  O(m * n * l)
# Space: O(l)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        n, m = len(board[0]), len(board)
        lookup = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    lookup[i][j] = True
                    if self.DFS(i, j, board, lookup, word[1:]):
                        return True
                    lookup[i][j] = False
        return False
        
    def DFS(self, i, j, board, lookup, word):
        if not word:
            return True
        if i - 1 >= 0 and board[i - 1][j] == word[0] and not lookup[i - 1][j]:
            lookup[i - 1][j] = True
            if self.DFS(i - 1, j, board, lookup, word[1:]):
                return True
            lookup[i - 1][j] = False
        if i + 1 <= len(board) - 1 and board[i + 1][j] == word[0] and not lookup[i + 1][j]:
            lookup[i + 1][j] = True
            if self.DFS(i + 1, j, board, lookup, word[1:]):
                return True
            lookup[i + 1][j] = False
        if j - 1 >= 0 and board[i][j - 1] == word[0] and not lookup[i][j - 1]:
            lookup[i][j - 1] = True
            if self.DFS(i, j - 1, board, lookup, word[1:]):
                return True
            lookup[i][j - 1] = False
        if j + 1 <= len(board[0]) - 1 and board[i][j + 1] == word[0] and not lookup[i][j + 1]:
            lookup[i][j + 1] = True
            if self.DFS(i, j + 1, board, lookup, word[1:]):
                return True
            lookup[i][j + 1] = False
        return False

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        n, m = len(board[0]), len(board)
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.recur(board, visited, word, 0, i, j):
                    return True
        return False
        
    def recur(self, board, visited, word, cur, i, j):
        if len(word) == cur:
            return True
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or visited[i][j] or word[cur] != board[i][j]:
            return False
        visited[i][j] = True
        if self.recur(board, visited, word, cur + 1, i + 1, j) or \
        self.recur(board, visited, word, cur + 1, i - 1, j) or \
        self.recur(board, visited, word, cur + 1, i, j + 1) or \
        self.recur(board, visited, word, cur + 1, i, j - 1):
            return True
        visited[i][j] = False
        return False
    
if __name__ == '__main__':
    board = [
  "ABCE",
  "SFCS",
  "ADEE"
    ]
    #board = [['aa']]
    word1 = 'ABCCED'
    word2 = 'SEE'
    word3 = 'ABCB'
    word4 = 'NED'
    print(Solution().exist(board, word1))
