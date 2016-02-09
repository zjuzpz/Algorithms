"""
233. Number of Digit One
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.
"""
# O(logn)
# O(1)
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, index = 0, 1
        while n >= 10 ** (index - 1):
            right, left = n % (10 ** index), n // (10 ** index)
            if right >= 2 * (10 ** (index - 1)):
                res += (left + 1) * 10 ** (index - 1)
            elif right >= 10 ** (index - 1):
                res += left * 10 ** (index - 1) + right - 10 ** (index - 1) + 1
            else:
                res += left * 10 ** (index - 1)
            index += 1
        return res

class Solution2(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        num = "0" + str(n) + "0"
        index, res = 0, 0
        while index < len(num) - 2:
            left, mid, right = int(num[0 : index + 1]), int(num[index + 1]), int(num[index + 2 :]) // 10
            if mid == 0:
                res += left * 10 ** (len(num) - 3 - index)
            elif mid == 1:
                res += left * 10 ** (len(num) - 3 - index) + right + 1
            else:
                res += (left + 1) * 10 ** (len(num) - 3 - index)
            index += 1
        return res

if __name__ == "__main__":
    print(Solution().countDigitOne(68048))
    print(Solution().countDigitOne(1347))
