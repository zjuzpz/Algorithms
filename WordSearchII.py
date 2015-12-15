"""
212. Word Search II
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
# O(m * n * l) 
# O(m * n)
class Trie(object):
    def __init__(self):
        self.leave = {}
        self.isString = False
        
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.leave:
                cur.leave[c] = Trie()
            cur = cur.leave[c]
        cur.isString = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return
        lookup = Trie()
        for word in words:
            lookup.insert(word)
        m, n = len(board), len(board[0])
        res, visited = set(), [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self.recur(res, visited, i, j, board, lookup, [board[i][j]])
        return list(res)
        
    def recur(self, res, visited, x, y, board, lookup, cur):
        if board[x][y] not in lookup.leave:
            return 
        if visited[x][y]:
            return
        if lookup.leave[board[x][y]].isString:
            res.add("".join(cur))
        visited[x][y] = True
        next_node = lookup.leave[board[x][y]]
        if x > 0:
            self.recur(res, visited, x - 1, y, board, next_node, cur + [board[x - 1][y]])
        if x < len(board) - 1:
            self.recur(res, visited, x + 1, y, board, next_node, cur + [board[x + 1][y]])
        if y > 0:
            self.recur(res, visited, x, y - 1, board, next_node, cur + [board[x][y - 1]])
        if y < len(board[0]) - 1:
            self.recur(res, visited, x, y + 1, board, next_node, cur + [board[x][y + 1]])
        visited[x][y] = False

if __name__ == "__main__":
    words = ["oath", "pea", "eat", "rain"]
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],\
             ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    print(Solution().findWords(board, words))
