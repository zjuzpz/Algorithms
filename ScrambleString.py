"""
87. Scramble String
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""
# O(n ^ 4)
# O(n ^ 3)
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        res = [[[False for j in range(len(s1))] for i in range(len(s2))] for k in range(len(s1) + 1)]
        for i in range(len(s2)):
            for j in range(len(s1)):
                if s2[i] == s1[j]:
                    res[1][i][j] = True
        for k in range(2, len(res)):
            for i in range(len(s2) - k + 1):
                for j in range(len(s1) - k + 1):
                    for p in range(1, k):
                        if res[p][i][j] and res[k - p][i + p][j + p] or \
                        res[p][i][j + k - p] and res[k - p][i + p][j]:
                            res[k][i][j] = True
                            break
        return res[-1][0][0]

if __name__ == "__main__":
    print(Solution().isScramble("rgeat", "rgtae"))
