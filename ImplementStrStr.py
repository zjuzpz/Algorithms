"""
28. Implement strStr().
Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""
# O(m * n)
# O(1)
# Also you can use KMP algorithm, whose complexity: O(m + n) and O(m)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        lookup = {needle:True}
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] in lookup:
                return i
        return -1

if __name__ == "__main__":
    haystack = "abccddc"
    needle = "cd"
    print(Solution().strStr(haystack, needle))
