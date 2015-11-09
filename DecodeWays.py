"""
91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
# O(n)
# O(n)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        res = [0 for i in range(len(s) + 1)]
        res[0], res[1] = 1, 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] in "12":
                    res[i + 1] = res[i - 1]
                else:
                    return 0
            elif s[i] in "123456":
                if s[i - 1] in "12":
                    res[i + 1] = res[i] +  res[i - 1]
                else:
                    res[i + 1] = res[i]
            else:
                if s[i - 1] == "1":
                    res[i + 1] = res[i] + res[i - 1]
                else:
                    res[i + 1] = res[i]
        return res[-1]

if __name__ == "__main__":
    print(Solution().numDecodings("12613910"))
