"""
125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""
# O(n)
# O(1)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                i, j = i + 1, j - 1
            else:
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome("asdfdsa"))
