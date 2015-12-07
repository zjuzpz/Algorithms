"""
171. Excel Sheet Column Number
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""
# O(n)
# O(1)
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {chr(ord("A") + i) : i + 1 for i in range(0, 26)}
        j, res, index = len(s) - 1, 0, 0
        while j >= 0:
            res += lookup[s[j]] * 26 ** index
            index += 1
            j -= 1
        return res

if __name__ == "__main__":
    print(Solution().titleToNumber("AZX"))
