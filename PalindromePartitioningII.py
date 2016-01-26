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
        lookup = [[True for j in s] for i in s]
        for i in range(1, len(s)):
            for j in range(i):
                if s[j] != s[i]:
                    lookup[i][j] = False
                else:
                    lookup[i][j] = lookup[i - 1][j + 1]
        res = [float("inf") for i in range(len(s))]
        for i in range(len(s)):
            if lookup[i][0]:
                res[i] = 0
            else:
                for j in range(i):
                    if lookup[i][j + 1]:
                        res[i] = min(res[i], res[j] + 1)
        return res[-1]

class Solution3(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = [[False for j in s] for i in s]
        for i in reversed(range(len(s))):
            lookup[i][i] = True
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (j - i <= 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
        res = [float("inf") for i in range(len(s))]
        for i in range(len(s)):
            if lookup[0][i]:
                res[i] = 0
            else:
                for j in range(i):
                    if lookup[j + 1][i]:
                        res[i] = min(res[i], res[j] + 1)
        return res[-1]
    
if __name__ == "__main__":
    s = "abbab"
    print(Solution3().minCut(s))
