"""
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""
# O(logn)
# O(1)
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, index = 0, 31
        while n > 0:
            res += (n % 2) * 2 ** index
            n //= 2
            index -= 1
        return res

if __name__ == "__main__":
    num = 43261596
    print(Solution().reverseBits(num))
