"""
231. Power of Two
Given an integer, write a function to determine if it is a power of two.
"""
# O(log2)
# O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 1:
                return False
            n //= 2
        return True

# O(1)
# O(1)
class Solution2(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0

# O(1)
# O(1)
class Solution3(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n ^ (n - 1) == (n << 1) - 1

if __name__ == "__main__":
    print(Solution3().isPowerOfTwo(32))
