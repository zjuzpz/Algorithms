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
# O(1) It is because from a to z, the maximum possible distinct pattern we have is 26 
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        map_ps, map_sp, count = {}, {}, 0
        word = str.split(" ")
        if len(word) != len(pattern):
            return False
        for i in range(len(pattern)):
            p, s = pattern[i], word[i]
            if p in map_ps and map_ps[p] != s:
                return False
            if p not in map_ps:
                if s not in map_sp:
                    map_ps[p], map_sp[s] = s, p
                else:
                    return False
        return True


if __name__ == "__main__":
    print(Solution().wordPattern("abba", "cat dog dog cat"))
