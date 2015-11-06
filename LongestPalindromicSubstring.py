"""
5. Longest Palindromic Substring
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
"""
# O(n)
# O(n)
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s_p = self.preProcess(s)
        center, right, max_index, res = 0, 0, 0, [0 for i in range(len(s_p))]
        for i in range(1, len(s_p) - 1):
            if i < right:
                i_mirror = 2 * center - i
                res[i] = min(right - i, res[i_mirror])
            while s_p[i - 1 - res[i]] == s_p[i + 1 + res[i]]:
                res[i] += 1
            if res[i] > res[max_index]:
                max_index = i
            if res[i] + i > right:
                right = res[i] + i
                center = i
        index = (max_index - 1 - res[max_index]) // 2
        return s[index: index + res[max_index]]
        
    def preProcess(self, s):
        res = "^"
        for i in s:
            res += "#" + i
        res += "#$"
        return res
            
if __name__ == "__main__":
    s = "abcbad"
    print(Solution().longestPalindrome(s))
