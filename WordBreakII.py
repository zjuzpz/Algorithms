"""
140. Word Break II
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
# O(2 ^ n)
# O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        path = [[] for i in range(len(s) + 1)]
        path[0] = [0]
        for i in range(len(s)):
            for j in range(0, i + 1):
                if path[j] and s[j : i + 1] in wordDict:
                    path[i + 1].append(j)
        if not path[-1]:
            return []
        res = []
        self.traceBack(res, path, "", len(s), s)
        return res
        
    def traceBack(self, res, path, cur, prev, s):
        if prev == 0:
            res.append(cur[:len(cur) - 1])
        else:
            for i in path[prev]:
                self.traceBack(res, path, s[i : prev] + " " + cur, i, s)

if __name__ == "__main__":
    s = "catsanddog"
    wordDict = set(["cat", "cats", "and", "sand", "dog"])
    print(Solution().wordBreak(s, wordDict))
