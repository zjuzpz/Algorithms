"""
258. Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
# O(1)
# O(1)
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            tem = 0
            while num >= 10:
                tem += num % 10
                num //= 10
            num += tem
        return num

class Solution2(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else (num - 1) % 9 + 1

if __name__ == "__main__":
    print(Solution().addDigits(987602918))
    print(Solution2().addDigits(987602918))    
