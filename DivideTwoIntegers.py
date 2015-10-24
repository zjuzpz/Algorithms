"""
29. Divide Two Integers
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
"""
# O(logn)
# O(1)
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        if dividend >= 0 and divisor > 0 or (dividend <= 0 and divisor < 0):
            flag = 1
        else:
            flag = -1
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            tem, count = divisor, 1
            while dividend >= tem:
                tem <<= 1
                count <<= 1
            dividend -= tem >> 1
            res += count >> 1
        if flag == -1:
            res == -res
        if res < -2 ** 31:
            return -2 ** 31
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res

if __name__ == "__main__":
    print(Solution().divide(-2001, 50))
