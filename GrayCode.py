"""
89. Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
"""
# O(2^n)
# O(1)
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]
        res, index = [0, 1], 1
        while n > 1:
            n -= 1
            tem = [i + 2 ** index for i in res]
            tem.reverse()
            res += tem
            index += 1
        return res

if __name__ == "__main__":
    print(Solution().grayCode(4))
