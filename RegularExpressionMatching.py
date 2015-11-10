"""
10. Regular Expression Matching
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
# O(m * n)
# O(m * n)
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        res = [[False for j in range(len(s) + 1)] for i in range(len(p) + 1)]
        res[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                res[i][0] = res[i - 2][0]
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == ".":
                    res[i][j] = res[i - 1][j - 1]
                elif p[i - 1] == "*":
                    if res[i - 1][j] or res[i - 2][j]:
                        res[i][j] = True
                    elif (p[i - 2] == s[j - 1] or p[i - 2] == ".") and res[i][j - 1]:
                        res[i][j] = True
        return res[-1][-1]

if __name__ == "__main__":
    s = "aab"
    p = "c*a*b"
    print(Solution().isMatch(s, p))
