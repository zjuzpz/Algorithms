"""
30. Substring with Concatenation of All Words
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
# O(n * m * k) m is the length of each word and k is the num of total words
# O(m * k)
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        lookup = {}
        for word in words:
            if word not in lookup:
                lookup[word] = 1
            else:
                lookup[word] += 1
        res, length = [], len(words[0])
        for i in range(0, len(s) - len(words) * length + 1):
            if self.isSubString(dict.copy(lookup), s[i : i + len(words) * length], length):
                res.append(i)
        return res
        
    def isSubString(self, lookup, s, length):
        i = 0
        while i <= len(s) - length:
            word = s[i : i + length]
            if word not in lookup:
                return False
            lookup[word] -= 1
            if lookup[word] < 0:
                return False
            i += length
        return True

if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(Solution().findSubstring(s, words))
