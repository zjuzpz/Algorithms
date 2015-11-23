"""
231. Power of Two
Given an integer, write a function to determine if it is a power of two.
"""
# O(logn)
# O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        num = 1
        while num <= n:
            if n == num:
                return True
            num <<= 1
        return False

# O(1)
# O(1)
class Solution2:
    """
    :type n: int
    :rtype: bool
    """
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0

if __name__ == '__main__':
    n = -2
    print(Solution().isPowerOfTwo(n))
