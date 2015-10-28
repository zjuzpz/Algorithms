"""
204. Count Primes
Description:
Count the number of prime numbers less than a non-negative number, n.
"""
# O(n)
# O(n)
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        lookup = [True for i in range(n)]
        res = 0
        for i in range(2, n):
            if lookup[i]:
                res += 1
                self.setFalse(i, n, lookup)
        return res
        
    def setFalse(self, i, n, lookup):
        tem = i;
        i += tem
        while i < n:
            lookup[i] = False
            i += tem

if __name__ == "__main__":
    print(Solution().countPrimes(10))
