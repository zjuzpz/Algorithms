"""
260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
# O(n)
# O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = 0
        for num in nums:
            n ^= num
        index = 0
        while True:
            if n % 2 == 1:
                break
            n //= 2
            index += 1
        res1, res2 = 0, 0
        for num in nums:
            if num // (2 ** index) % 2 == 1:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]

if __name__ == "__main__":
    print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
