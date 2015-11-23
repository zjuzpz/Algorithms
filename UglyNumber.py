"""
263. Ugly Number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""
# O(logn)
# O(1)
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num >= 2:
            tem = num
            if num % 5 == 0:
                num //= 5
            if num % 3 == 0:
                num //= 3
            if num % 2 == 0:
                num //= 2
            if num == tem:
                return False
        return True

class Solution2(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i
        return num == 1
    
if __name__ == "__main__":
    print(Solution().isUgly(14))
