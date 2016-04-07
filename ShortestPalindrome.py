"""
214. Shortest Palindrome
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

# O(n)
# O(n)
# Manacher's algorithm
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_p = self.preProcess(s)
        center, maxIndex, right, res = 0, 0, 0, [0 for i in range(len(s_p))]
        for i in range(1, len(s_p) - 1):
            if i < right:
                i_mirror = 2 * center - i
                res[i] = min(right - i, res[i_mirror])
            while s_p[i - 1 - res[i]] == s_p[i + 1 + res[i]]:
                res[i] += 1
            if i - res[i] == 1 and res[i] > res[maxIndex]:
                maxIndex = i
            if i + res[i] > right:
                right = i + res[i]
                center = i
        right = s[res[maxIndex]:]
        left = right[::-1]
        return left + s
        
        
    def preProcess(self, s):
        res = ["^"]
        for ss in s:
            res.append("#")
            res.append(ss)
        res.append("#")
        res.append("$")
        return "".join(res)

# O(n ^ 2)
# O(1)
class Solution2(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        maxLength, i = 1, 0
        while i < len(s):
            j, k = i, i
            while k < len(s) - 1 and s[k] == s[k + 1]:
                k += 1
            i = k + 1
            while j >= 1 and k < len(s) - 1 and s[j - 1] == s[k + 1]:
                j, k = j - 1, k + 1
            if j == 0:
                maxLength = max(maxLength, k + 1)
        tem = s[maxLength:]
        tem = tem[::-1]
        return tem + s

    
if __name__ == "__main__":
    print(Solution().shortestPalindrome("aacecaaa"))
    print(Solution().shortestPalindrome("a"))
    print(Solution().shortestPalindrome("abcd"))
