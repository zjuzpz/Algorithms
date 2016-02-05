"""
137. Single Number II
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
# O(n)
# O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0 for i in range(33)]
        for num in nums:
            i, n = 1, num
            if n < 0:
                bits[0] += 1
                bits[0] %= 3
                n = -n
            while n > 0:
                if n % 2 == 1:
                    bits[i] += 1
                    bits[i] %= 3
                n //= 2
                i += 1
        res = 0
        for i in range(1, 33):
            res += 2 ** (i - 1) * bits[i]
        return res if bits[0] == 0 else -res

class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0, 0, 0
        for num in nums:
            two |= one & num
            one ^= num
            three = two & one
            one &= ~three
            two &= ~three
        return one

if __name__ == "__main__":
    print(Solution().singleNumber([-1, 3, 4, 3, -1, -2, 4, 3, 4, -1]))
