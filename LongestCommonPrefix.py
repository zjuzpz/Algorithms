"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = 0
        while True:
            for i in range(len(strs)):
                if res >= len(strs[i]):
                    return strs[0][0 : res]
                if strs[i][res] != strs[0][res]:
                    return strs[0][0 : res]
            res += 1

if __name__ == "__main__":
    strs = ["asc", "as", "a"]
    print(Solution().longestCommonPrefix(strs))
