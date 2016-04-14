"""
336. Palindrome Pairs
Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
# O(n * k ^ 2)
# O(n)
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lookup, res = {}, []
        for i in range(len(words)):
            lookup[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                prefix = words[i][:j]
                suffix = words[i][j:]
                if j > 0 and self.isPalin(prefix) and suffix[::-1] in lookup and lookup[suffix[::-1]] != i:
                    res.append([lookup[suffix[::-1]], i])
                if self.isPalin(suffix) and prefix[::-1] in lookup and lookup[prefix[::-1]] != i:
                    res.append([i, lookup[prefix[::-1]]])
        return res
        
    def isPalin(self, word):
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i, j =i + 1, j - 1
        return True

if __name__ == "__main__":
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    print(Solution().palindromePairs(words))
