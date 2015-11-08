"""
72. Edit Distance
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
# O(m * n)
# O(m * n)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return max(len(word1), len(word2))
        res = [[float('inf') for j in range(len(word1) + 1)] for i in range(len(word2) + 1)] 
        for j in range(len(word1) + 1):
            res[0][j] = j
        for i in range(len(word2) + 1):
            res[i][0] = i
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word2[i - 1] != word1[j - 1]:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j], res[i][j - 1]) + 1
                else:
                    res[i][j] = res[i - 1][j - 1]
        return res[-1][-1]

if __name__ == "__main__":
    word1 = "zoologicoarchaeologist"
    word2 = "zoogeologist" 
    print(Solution().minDistance(word1, word2))
