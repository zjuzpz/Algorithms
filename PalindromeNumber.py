"""
9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
"""
# O(1)
# O(1)
#For all
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tem, count = x, 1
        while tem >= 10:
            tem //= 10
            count += 1
        tem = count
        count = 1
        while count <= tem // 2:
            right = str(x % 10 ** count)
            left = str(x // 10 ** (tem - count))
            if len(right) != len(left):
                if left[-1] == '0':
                    count += 1
                    continue
                else:
                    return False
            elif left[-1] != right[0]:
                return False
            count += 1
        return True

#Only for python, because there is no overflow problem
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0
        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10
        return x == reverse
