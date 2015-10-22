"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
"""
# O(n)
# O(n)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack, lookup = [], {')':'(', ']':'[', '}':'{'}
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if lookup[s[i]] != stack.pop():
                    return False
        return not stack

if __name__ == "__main__":
    s = "(){(})"
    print(Solution().isValid(s))
