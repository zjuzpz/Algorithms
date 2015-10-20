"""
7. Reverse Integer
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
            s = str(x)[1:]
        else:
            s = str(x)
        i, res = 0, 0
        while i < len(s):
            res += int(s[i]) * 10 ** i
            i += 1
        res *= flag
#Actually, for python, the res won't be overflow
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res

if __name__ == "__main__":
    x1 = -123
    x2 = 2**31 - 1
    print(Solution().reverse(x1))
    print(Solution().reverse(x2))
