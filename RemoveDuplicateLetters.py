"""
316. Remove Duplicate Letters
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
# O(n)
# O(1)
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lookup = {chr(ord("a") + i) : 0 for i in range(26)}
        for a in s:
            lookup[a] += 1
        stack, visited = [], set()
        for a in s:
            lookup[a] -= 1
            if a not in visited:
                while stack and stack[-1] > a and lookup[stack[-1]] > 0:
                    visited.remove(stack.pop())
                visited.add(a)
                stack.append(a)
        return "".join(stack)

if __name__ == "__main__":
    s = "cbacdcbc"
    print(Solution().removeDuplicateLetters(s))
