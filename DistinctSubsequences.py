"""
115. Distinct Subsequences
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""
# O(m * n)
# O(m * n)
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0
        if len(t) == 0:
            return 1
        m, n = len(t), len(s)
        res = [[0 for j in range(n)] for i in range(m)]
        if s[0] == t[0]:
            res[0][0] = 1
        for j in range(1, n):
            if t[0] == s[j]:
                res[0][j] = res[0][j - 1] + 1
            else:
                res[0][j] = res[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if t[i] == s[j]:
                    res[i][j] = res[i][j - 1] + res[i - 1][j - 1]
                else:
                    res[i][j] = res[i][j - 1]
        return res[-1][-1]

if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"
    print(Solution().numDistinct(s, t))
