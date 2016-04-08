"""
269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
# O(n)
# O(n)
from collections import deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        lookup, allLetters = {}, set()
        for i in range(len(words) - 1):
            edge = self.findEdge(words[i], words[i + 1])
            if edge is not None:
                if edge[0] not in lookup:
                    lookup[edge[0]] = set()
                lookup[edge[0]].add(edge[1])
            for letter in words[i]:
                allLetters.add(letter)
        for letter in words[-1]:
            allLetters.add(letter)
        res, sortedLetters = deque(), set()
        for letter in allLetters:
            if letter not in lookup:
                sortedLetters.add(letter)
                res.appendleft(letter)
        visited = set()
        for key in lookup:
            if key not in sortedLetters:
                visited.add(key)
                if not self.DFS(res, sortedLetters, key, lookup, visited):
                    return ""
                visited.remove(key)
                sortedLetters.add(key)
                res.appendleft(key)
        return list(res)
        
    def DFS(self, res, sortedLetters, key, lookup, visited):
        for letter in lookup[key]:
            if letter in visited:
                return False
            visited.add(letter)
            if letter not in sortedLetters:
                if not self.DFS(res, sortedLetters, letter, lookup, visited):
                    return False
                sortedLetters.add(letter)
                res.appendleft(letter)
            visited.remove(letter)
        return True
        
    def findEdge(self, word1, word2):
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return (word1[i], word2[i])
                

if __name__ == "__main__":
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(Solution().alienOrder(words))
