"""
66. Plus One
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
# O(n)
# O(1)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        j = len(digits) - 1
        carry = 1
        while j >= 0:
            digits[j] += carry
            carry = digits[j] // 10
            digits[j] %= 10
            if carry == 0:
                return digits
            j -= 1
        digits.insert(0, 1)
        return digits

if __name__ == "__main__":
    print(Solution().plusOne([9,9,9]))
