"""
245. Shortest Word Distance III
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""
# O(n)
# O(1)
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return self.helper(words, word1)
        res, index1, index2 = float("inf"), -float("inf"), -float("inf")
        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
                res = min(res, index1 - index2)
            elif words[i] == word2:
                index2 = i
                res = min(res, index2 - index1)
        return res
        
    def helper(self, words, word1):
        res, index = float("inf"), -float("inf")
        for i in range(len(words)):
            if words[i] == word1:
                res = min(res, i - index)
                index = i
        return res

if __name__ == "__main__":
    word1 = "makes"
    word2 = "coding"
    words = ["practice", "makes", "makes", "practice", "coding"]
    print(Solution().shortestWordDistance(words, word1, word2))
