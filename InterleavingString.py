"""
97. Interleaving String
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""
# O(m * n)
# O(max(m, n))
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        previous, cur = [], []
        previous.append(True)
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s3[j - 1] and previous[-1]:
                previous.append(True)
            else:
                previous.append(False)
        for i in range(1, len(s2) + 1):
            for j in range(len(s1) + 1):
                if s3[i + j - 1] == s2[i - 1] and previous[j]:
                    cur.append(True)
                elif j > 0 and s3[i + j - 1] == s1[j - 1] and cur[-1]:
                    cur.append(True)
                else:
                    cur.append(False)
            previous, cur = cur, []
        return previous[-1]

if __name__ == "__main__":
    print(Solution().isInterleave("", "abc", "abc"))
    print(Solution().isInterleave("db", "b", "cbb"))
