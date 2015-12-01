"""
201. Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""
# O(1)
# O(1)
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        mb, nb = bin(m)[2:], bin(n)[2:]
        if len(mb) != len(nb):
            return res
        length = len(mb)
        for i in range(length):
            if mb[i] == nb[i] == "1":
                res += 2 ** (length - 1 - i)
            elif mb[i] != nb[i]:
                return res
        return res

if __name__ == "__main__":
    print(Solution().rangeBitwiseAnd(5,7))
