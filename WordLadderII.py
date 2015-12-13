"""
126. Word Ladder II
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""
# O(n * d) n is the length of string
# O(d)
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordlist.add(beginWord)
        wordlist.add(endWord)
        res, cur, found, visited, path = [], [beginWord], False, set(), {word:[] for word in wordlist}
        while not found and cur:
            next_turn = set()
            for word in cur:
                visited.add(word)
            for word in cur:
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[0 : i] + j + word[i + 1:]
                        if candidate == endWord:
                            found = True
                        if candidate not in visited and candidate in wordlist:
                            path[candidate].append(word)
                            next_turn.add(candidate)
            cur = next_turn
        if found:
            self.traceBack(res, [], path, endWord)
        return res
        
    def traceBack(self, res, cur, path, word):
        if not path[word]:
            res.append([word] + cur)
        else:
            for prev in path[word]:
                self.traceBack(res, [word] + cur, path, prev)

if __name__ == "__main__":
    begin = "hot"
    end = "dog"
    dict = set(["hot", "dog", "dot"])
    print(Solution().findLadders(begin, end, dict))
