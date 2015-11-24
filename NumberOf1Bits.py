"""
191. Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""
# O(logn)
# O(1)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        res = 0
        while n > 0:
            res += n % 2
            n //= 2
        return res

class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

if __name__ == "__main__":
    print(Solution().hammingWeight(11))
