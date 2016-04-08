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
        edges, allLetter = [], set()
        for i in range(len(words) - 1):
            self.findEdge(edges, words[i], words[i + 1])
            for j in words[i]:
                allLetter.add(j)
        for j in words[-1]:
            allLetter.add(j)
            
        lookup = {}
        for edge in edges:
            if edge[0] not in lookup:
                lookup[edge[0]] = set([edge[1]])
            else:
                lookup[edge[0]].add(edge[1])
        
        res, sortedLetter = deque(), set()
        for letter in allLetter:
            if letter not in lookup:
                res.appendleft(letter)
                sortedLetter.add(letter)
    
        for key in lookup:
            visited = set()
            visited.add(key)
            if not self.DFS(lookup, visited, key, res, sortedLetter):
                return ""
            if key not in sortedLetter:
                res.appendleft(key)
                sortedLetter.add(key)
        return list(res)
        
    def findEdge(self, edges, word1, word2):
        for i in range(len(min(word1, word2))):
            if word1[i] != word2[i]:
                edges.append([word1[i], word2[i]])
                return
            
    def DFS(self, lookup, visited, key, res, sortedLetter):
        for letter in lookup[key]:
            if letter not in sortedLetter and letter in lookup:
                if letter in visited:
                    return False
                visited.add(letter)
                if not self.DFS(lookup, visited, letter, res, sortedLetter):
                    return False
                visited.remove(letter)
                if letter not in sortedLetter:
                    res.appendleft(letter)
                    sortedLetter.add(letter)
        return True
                

if __name__ == "__main__":
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(Solution().alienOrder(words))
