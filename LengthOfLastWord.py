"""
58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""
# O(n)
# O(1)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        j, length = len(s) - 1, 0
        while j >= 0:
            if s[j] == " " and length == 0:
                j -= 1
            elif s[j] != " ":
                length += 1
                j -= 1
            else:
                return length
        return length

if __name__ == "__main__":
    print(Solution().lengthOfLastWord(" hello world  "))
