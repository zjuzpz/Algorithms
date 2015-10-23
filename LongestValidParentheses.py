"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
# O(n)
# O(n)
# There is also some ways: O(n), O(1)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        record = [False for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif stack:
                record[stack.pop()] = True
                record[i] = True
        res, cur = 0, 0
        for i in range(len(record)):
            if record[i]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
        return max(res, cur)

if __name__ == "__main__":
    print(Solution().longestValidParentheses("()(()()"))
