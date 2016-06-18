"""
357. Count Numbers with Unique Digits
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""
# O(1)
# O(1)
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        res = 10
        cur = 9
        count = 9
        while n > 1:
            n -= 1
            cur *= count
            res += cur
            count -= 1
            if not count:
                break
        return res

if __name__ == "__main__":
    print(Solution().countNumbersWithUniqueDigits(2))
