"""
44. Wildcard Matching
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
# O(m * n)
# O(m * n)
# LTE
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
                res[i][0] = True
            else:
                break
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == "?":
                    res[i][j] = res[i - 1][j - 1]
                elif p[i - 1] == "*" and (res[i - 1][j - 1] or res[i - 1][j] or res[i][j - 1]):
                    res[i][j] = True
        return res[-1][-1]

# O(m + n)
# O(1)
class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_cur, s_cur, p_last, s_last = 0, 0, -1, - 1
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == "?"):
                p_cur, s_cur = p_cur + 1, s_cur + 1
            elif p_cur < len(p) and p[p_cur] == "*":
                p_cur += 1
                p_last, s_last = p_cur, s_cur
            elif p_last != -1:
                s_last += 1
                p_cur, s_cur = p_last, s_last
            else:
                return False
        while p_cur < len(p) and p[p_cur] == "*":
            p_cur += 1
        return p_cur == len(p)

if __name__ == "__main__":
    s = "abacddb"
    p = "a?a*d*db"
    print(Solution().isMatch(s, p))
