"""
168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""
# O(logn)
# O(1)
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        lookup = {i : chr(ord('A') - 1 + i) for i in range(1, 27)}
        res = ""
        while n > 0:
            tem = n % 26
            if tem == 0:
                res = lookup[26] + res
                n //= 26
                n -= 1
            else:
                res = lookup[tem] + res
                n //= 26
        return res

if __name__ == "__main__":
    print(Solution().convertToTitle(26 * 26))
