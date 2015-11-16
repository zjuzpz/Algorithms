"""
139. Word Break
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
# O(n ^ 2)
# O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        res = [False for i in range(len(s))]
        for i in range(len(s)):
            if s[0 : i + 1] in wordDict:
                res[i] = True
            else:
                j = 0
                while j < i:
                    if res[j] and s[j + 1: i + 1] in wordDict:
                        res[i] = True
                        break
                    j += 1
        return res[-1]

if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", {"leet", "code"}))
