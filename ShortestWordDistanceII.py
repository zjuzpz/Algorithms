"""
244. Shortest Word Distance II
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
# O(n) for init  O(m + n) for lookup
# O(n)
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.lookup = {}
        for i in range(len(words)):
            if words[i] not in self.lookup:
                self.lookup[words[i]] = [i]
            else:
                self.lookup[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.lookup[word1], self.lookup[word2]
        i, j, res = 0, 0, float("inf")
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                res = min(res, l2[j] - l1[i])
                i += 1
            else:
                res = min(res, l1[i] - l2[j])
                j += 1
        return res

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    w = WordDistance(words)
    print(w.shortest("coding", "practice"))
