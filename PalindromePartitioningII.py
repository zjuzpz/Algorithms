"""
132. Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
# O(n ^ 3)
# O(n)
# LTE
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [float("inf") for i in range(len(s))]
        res[0] = 1
        for i in range(1, len(s)):
            if self.isPalindrome(s[0 : i + 1]):
                res[i] = 1
            else:
                for j in range(i):
                    if self.isPalindrome(s[j + 1 : i + 1]):
                        res[i] = min(res[i], res[j] + 1)
        return res[-1]
        
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True

"""
Use dp to make a lookup table first to reduce time complexity
"""
# O(n ^ 2)
# O(n ^ 2)
class Solution2(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = [[False for j in s] for i in s]
        for i in reversed(range(len(s))):
            for j in range(len(s)):
                if i >= j:
                    lookup[i][j] = True
                elif s[i] == s[j] and lookup[i + 1][j - 1]:
                    lookup[i][j] = True
        res = [float("inf") for i in s]
        for i in range(len(s)):
            if lookup[0][i]:
                res[i] = 0
            else:
                for j in range(1, i + 1):
                    if lookup[j][i]:
                        res[i] = min(res[i], res[j - 1] + 1)
        return res[-1]
    
if __name__ == "__main__":
    s = "abbab"
    print(Solution2().minCut(s))
