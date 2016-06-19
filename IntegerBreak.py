"""
343. Integer Break
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.
"""
# O(logn) (pow is logn)
# O(1)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        res, reminder = n // 3, n % 3
        if reminder == 0:
            return 3 ** res
        if reminder == 1:
            return 3 ** (res - 1) * 4
        return 3 ** res * 2

if __name__ == "__main__":
    print(Solution().integerBreak(10))
