"""
243. Shortest Word Distance
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
# O(n)
# O(1)
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lookup, res = {}, float("inf")
        lookup[word1], lookup[word2] = None, None
        for i in range(len(words)):
            if words[i] == word1:
                lookup[word1] = i
                if lookup[word2] is not None:
                    res = min(res, lookup[word1] - lookup[word2])
            elif words[i] == word2:
                lookup[word2] = i
                if lookup[word1] is not None:
                    res = min(res, lookup[word2] - lookup[word1])
        return res

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(Solution().shortestDistance(words, word1, word2))
