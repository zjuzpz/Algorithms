"""
338. Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
# O(n)
# O(1)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if not num:
            return [0]
        base, cur, res = 1, 1, [0, 1]
        for i in range(1, num):
            if base == cur:
                res.append(1)
                base = len(res) - 1
                cur = 1
            else:
                res.append(1 + res[cur])
                cur += 1
        return res

class Solution2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, num + 1):
            res.append((i & 1) + res[i // 2])
        return res

if __name__ == "__main__":
    print(Solution().countBits(10))
