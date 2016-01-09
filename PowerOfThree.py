"""
326. Power of Three
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
# O(logn)
# O(1)
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3
        return True

# O(1)
# O(1)
class Solution2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** 19 % n == 0

if __name__ == "__main__":
    print(Solution().isPowerOfThree(3 ** 15))
