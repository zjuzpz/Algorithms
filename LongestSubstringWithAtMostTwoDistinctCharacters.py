"""
159. Longest Substring with At Most Two Distinct Characters
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
"""
# O(n)
# O(1)
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup, start, cur, res = {}, 0, 0, 0
        while cur < len(s):
            if s[cur] in lookup:
                lookup[s[cur]] += 1
            elif len(lookup) < 2:
                lookup[s[cur]] = 1
            else:
                res = max(res, cur - start)
                while True:
                    lookup[s[start]] -= 1
                    if lookup[s[start]] == 0:
                        del lookup[s[start]]
                        start += 1
                        break
                    start += 1
                lookup[s[cur]] = 1
            cur += 1
        res = max(res, cur - start)
        return res

if __name__ == "__main__":
    s = "eceba"
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))
