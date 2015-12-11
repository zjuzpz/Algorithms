"""
264. Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
"""
# O(n)
# O(n)
from collections import deque
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, l2, l3, l5 = 1, deque([2]), deque([3]), deque([5])
        while n > 1:
            n -= 1
            res = min(l2[0], l3[0], l5[0])
            if res == l2[0]:
                l2.popleft()
            if res == l3[0]:
                l3.popleft()
            if res == l5[0]:
                l5.popleft()
            l2.append(res * 2)
            l3.append(res * 3)
            l5.append(res * 5)
        return res
if __name__ == "__main__":
    for i in range(1, 20):
        print(Solution().nthUglyNumber(i))
