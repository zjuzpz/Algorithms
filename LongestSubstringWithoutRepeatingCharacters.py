"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""
# O(n)
# O(1)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, cur, lookup = 0, 0, {}
        for i in range(len(s)):
            if s[i] not in lookup:
                cur += 1
                lookup[s[i]] = i
            else:
                res = max(res, cur)
                if i - lookup[s[i]] > cur:
                    cur += 1
                else:
                    cur = i - lookup[s[i]]
                lookup[s[i]] = i
        return max(res, cur)

class Solution2:
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for i in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

if __name__ == "__main__":
    s = "abaabcdddabab"
    print(Solution().lengthOfLongestSubstring(s))
