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
        i, j, res = 0, 0, 0
        lookup = set()
        while j < len(s):
            if s[j] not in lookup:
                lookup.add(s[j])
            else:
                res = max(res, j - i)
                while s[i] != s[j]:
                    lookup.remove(s[i])
                    i += 1
                i += 1
            j += 1
        res = max(res, j - i)
        return res

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
