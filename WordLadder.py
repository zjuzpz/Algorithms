"""
127. Word Ladder
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""
# O(n * d)
# O(d)
import copy
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
        wordDict = copy.copy(wordList)
        wordDict.add(endWord)
        counter = 1
        cur = [beginWord]
        while cur:
            next = []
            counter += 1
            for word in cur:
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        new = word[0:i] + j + word[i + 1:]
                        if new in wordDict:
                            if new == endWord:
                                return counter
                            next.append(new)
                            wordDict.remove(new)
            cur = next
        return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = set(["hot", "dot", "dog", "lot", "log"])
    print(Solution().ladderLength(beginWord, endWord, wordList))
