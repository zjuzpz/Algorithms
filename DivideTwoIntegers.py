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
        dvd, dvs, res = abs(dividend), abs(divisor), 0
        while dvd >= dvs:
            tem, count = dvs, 1
            while dvd >= tem:
                count <<= 1
                tem <<= 1
            tem >>= 1
            count >>= 1
            res += count
            dvd -= tem
        if dividend > 0 and divisor < 0 or (dividend < 0 and divisor > 0):
            res = -res
        if res < -2 ** 31:
            return -2 ** 31
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res

if __name__ == "__main__":
    print(Solution().divide(-2001, 50))
