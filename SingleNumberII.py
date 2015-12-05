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
        lookup = [0 for i in range(33)]
        for num in nums:
            if num < 0:
                num = -num
                lookup[32] += 1
                if lookup[32] == 3:
                    lookup[32] = 0
            index = 0
            while num > 0:
                lookup[index] += num % 2
                if lookup[index] == 3:
                    lookup[index] = 0
                num //= 2
                index += 1
        res, index = 0, 0
        for i in range(32):
            res += lookup[i] * 2 ** index
            index += 1
        if lookup[32] == 1:
            return -res
        return res
        
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
