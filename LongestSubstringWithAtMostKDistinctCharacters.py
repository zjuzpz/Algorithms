"""
340. Longest Substring with At Most K Distinct Characters
Given a string, find the length of the longest substring T that
contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""
# O(n)
# O(1)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k <= 0:
            return 0
        start, lookup, res = 0, {}, 1
        for i in range(len(s)):
            if len(lookup) == k and s[i] not in lookup:
                res = max(res, i - start)
                while start < i and lookup[s[start]] != start:
                    start += 1
                lookup.pop(s[start])
                start += 1
            lookup[s[i]] = i
        return max(res, len(s) - start)

# O(n)
# O(1)
class Solution2(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k <= 0:
            return 0
        start, lookup, res = 0, {}, 1
        for i in range(len(s)):
            if s[i] not in lookup and len(lookup) == k:
                res = max(res, i - start)
                left, c = float("inf"), None
                for key in lookup:
                    if lookup[key] < left:
                        left, c = lookup[key], key
                start = left + 1
                lookup.pop(c)
            lookup[s[i]] = i
        return max(res, len(s) - start)

if __name__ == "__main__":
    s = "eceba"
    k = 2
    print(Solution().lengthOfLongestSubstringKDistinct(s, k))
