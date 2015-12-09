"""
76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
# O(n)
# O(1)
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count_t, total_t = [0 for i in range(256)], 0
        count_s, total_s = [0 for i in range(256)], 0
        for i in t:
            count_t[ord(i)] += 1
            total_t += 1
        start, res = 0, ""
        for i in range(len(s)):
            count_s[ord(s[i])] += 1
            if count_s[ord(s[i])] <= count_t[ord(s[i])]:
                total_s += 1
            if total_s == total_t:
                while count_t[ord(s[start])] == 0 or count_s[ord(s[start])] > count_t[ord(s[start])]:
                    count_s[ord(s[start])] -= 1
                    start += 1
                if res == "" or i - start + 1 < len(res):
                    res = s[start : i + 1]
        return res

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = 'ABCC'
    print(Solution().minWindow(s,t))
