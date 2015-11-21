"""
290. Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""
# O(n)
# O(n)
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split()
        if len(l) != len(pattern):
            return False
        lookup1, lookup2 = {}, {}
        for i in range(len(pattern)):
            if pattern[i] not in lookup1:
                lookup1[pattern[i]] = l[i]
            elif lookup1[pattern[i]] != l[i]:
                return False
            if l[i] not in lookup2:
                lookup2[l[i]] = pattern[i]
            elif lookup2[l[i]] != pattern[i]:
                return False
        return True

# O(n)
# O(1)
class Solution2(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lookup1, lookup2, count = {}, {}, 0
        i, j = 0, 0
        while i < len(str):
            left = i
            while i < len(str) and str[i] != " ":
                i += 1
            word = str[left: i]
            if j >= len(pattern):
                return False
            if pattern[j] not in lookup1:
                lookup1[pattern[j]] = word
            elif lookup1[pattern[j]] != word:
                return False
            if word not in lookup2:
                count += 1
                if count > 26:
                    return False
                lookup2[word] = pattern[j]
            elif lookup2[word] != pattern[j]:
                return False
            i, j = i + 1, j + 1
        if j == len(pattern):
            return True
        return False

if __name__ == "__main__":
    print(Solution2().wordPattern("abba", "cat dog dog cat"))
