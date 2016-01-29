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
        self.leaf = {}
        self.isString = False
        
    def add(self, word):
        if not word:
            self.isString = True
            return
        cur = self
        for c in word:
            if c not in cur.leaf:
                cur.leaf[c] = Trie()
            cur = cur.leaf[c]
        cur.isString = True
            
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []
        lookup = Trie()
        for word in words:
            lookup.add(word)
        res, visited = set(), [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.DFS(res, [], lookup, board, i, j, visited)
        return list(res)
        
    def DFS(self, res, cur, lookup, board, x, y, visited):
        if board[x][y] not in lookup.leaf:
            return
        if visited[x][y]:
            return
        cur.append(board[x][y])
        visited[x][y] = True
        if lookup.leaf[board[x][y]].isString:
            res.add("".join(cur))
        if 0 <= x - 1:
            self.DFS(res, cur, lookup.leaf[board[x][y]], board, x - 1, y, visited)
        if x + 1 < len(board):
            self.DFS(res, cur, lookup.leaf[board[x][y]], board, x + 1, y, visited)
        if 0 <= y - 1:
            self.DFS(res, cur, lookup.leaf[board[x][y]], board, x, y - 1, visited)
        if y + 1 < len(board[0]):
            self.DFS(res, cur, lookup.leaf[board[x][y]], board, x, y + 1, visited)
        visited[x][y] = False
        cur.pop()

if __name__ == "__main__":
    words = ["oath", "pea", "eat", "rain"]
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],\
             ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    print(Solution().findWords(board, words))
