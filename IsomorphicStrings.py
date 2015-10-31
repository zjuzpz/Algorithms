"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
# O(n)
# O(1)
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lookup1, lookup2 = {}, {}
        for i in range(len(s)):
            if s[i] not in lookup1:
                lookup1[s[i]] = t[i]
            elif lookup1[s[i]] != t[i]:
                return False
            if t[i] not in lookup2:
                lookup2[t[i]] = s[i]
            elif lookup2[t[i]] != s[i]:
                return False
        return True

class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lookup, mapped = {}, set()
        for i in range(len(s)):
            if s[i] not in lookup:
                if t[i] in mapped:
                    return False
                lookup[s[i]] = t[i]
                mapped.add(t[i])
            elif lookup[s[i]] != t[i]:
                return False
        return True

if __name__ == "__main__":
    print(Solution().isIsomorphic("paper", "title"))
