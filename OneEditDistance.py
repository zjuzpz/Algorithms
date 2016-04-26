"""
161. One Edit Distance
Given two strings S and T,
determine if they are both one edit distance apart.
"""
# O(n)
# O(1)
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        if len(s) < len(t) - 1:
            return False
        if len(s) == len(t):
            return self.replace(s, t)
        return self.insert(s, t)
        
    def replace(self, s, t):
        replaced = False
        for i in range(len(s)):
            if s[i] != t[i]:
                if not replaced:
                    replaced = True
                else:
                    return False
        return replaced
        
    def insert(self, s, t):
        inserted = False
        i, j = 0, 0
        while i < len(s):
            if s[i] != t[j]:
                if not inserted:
                    inserted = True
                    j += 1
                else:
                    return False
            else:
                i, j = i + 1, j + 1
        return True

class Solution2(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        if len(s) < len(t) - 1 or s == t:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                if s[i:] == t[i + 1:] or s[i + 1:] == t[i + 1:]:
                    return True
                return False
        return True

if __name__ == "__main__":
    s, t = "leetcode", "leet code"
    print(Solution().isOneEditDistance(s, t))
