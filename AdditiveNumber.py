"""
306. Additive Number
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""
# O(n ^ 3)
# O(n)
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            num1 = int(num[0 : i + 1])
            for j in range(i + 1, len(num)):
                num2 = int(num[i + 1 : j + 1])
                if self.helper(num1, num2, num, str(num1) + str(num2), False):
                    return True
                if num2 == 0:
                    break
            if num1 == 0:
                return False
        return False
        
    def helper(self, num1, num2, num, cur, flag):
        if len(cur) >= len(num):
            if cur == num and flag:
                return True
            return False
        num1, num2 = num2, num1 + num2
        cur += str(num2)
        return self.helper(num1, num2, num, cur, True)

if __name__ == "__main__":
    print(Solution().isAdditiveNumber("199100199"))
