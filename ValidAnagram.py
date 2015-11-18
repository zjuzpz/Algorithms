"""
242. Valid Anagram
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters?
How would you adapt your solution to such case?
"""
# O(n)
# O(1)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = 1
            else:
                lookup[s[i]] += 1
            if t[i] not in lookup:
                lookup[t[i]] = -1
            else:
                lookup[t[i]] -= 1
        for key in lookup:
            if lookup[key] != 0:
                return False
        return True

if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))
