"""
342. Power of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""
# O(logn)
# O(1)
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num > 1:
            if num % 4 != 0:
                return False
            num //= 4
        return True

# O(logn)
# O(logn)
class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        if num % 4 != 0:
            return False
        return self.isPowerOfFour(num // 4)

# O(1)
# O(1)
class Solution3(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or num == 2:
            return False
        if num == 1:
            return True
        return num & (num - 1) == 0 and num & (0b01010101010101010101010101010101) == num

if __name__ == "__main__":
    print(Solution().isPowerOfFour(16))
