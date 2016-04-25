"""
344. Reverse String
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""
# O(n)
# O(n)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

if __name__ == "__main__":
    s = "hello"
    print(Solution().reverseString(s))
