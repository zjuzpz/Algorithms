"""
254. Factor Combinations
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""
# O(n^0.5logn)
# O(logn)
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.getPrime(res, [], 2, n)
        return res
        
    def getPrime(self, res, cur, start, n):
        for i in range(start, int(n ** 0.5) + 1):
            if n % i == 0:
                cur.append(i)
                cur.append(n // i)
                res.append(cur[:])
                cur.pop()
                self.getPrime(res, cur, i, n // i)
                cur.pop()

if __name__ == "__main__":
    print(Solution().getFactors(12))
