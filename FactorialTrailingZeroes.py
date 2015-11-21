"""
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
# O(logn)
# O(1)
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num, res = 5, 0
        while n >= num:
            res += n // num
            num *= 5
        return res

if __name__ == "__main__":
    print(Solution().trailingZeroes(1000))
