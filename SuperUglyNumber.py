"""
313.Super Ugly Number
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
"""
# O(k * n)
# O(k + n)
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res, lookup = [1], {primes[i] : 0 for i in range(len(primes))}
        for i in range(1, n):
            smallest, index = float("inf"), None
            for key in lookup:
                if key * res[lookup[key]] <= res[-1]:
                    lookup[key] += 1
                if key * res[lookup[key]] < smallest:
                    smallest = key * res[lookup[key]]
                    index = key
            res.append(smallest)
            lookup[index] += 1
        return res[-1]

if __name__ == "__main__":
    primes = [2, 3, 5]
    n = 2
    print(Solution().nthSuperUglyNumber(n, primes))
