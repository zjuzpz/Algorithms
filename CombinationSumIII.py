"""
216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""
# O(k * C(n, k))
# O(k)
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0 or k <= 0:
            return []
        res = []
        self.recur(res, [], k, n, 1)
        return res
        
    def recur(self, res, cur, k, n, start):
        if n == 0 and k == 0:
            res.append(cur[:])
            return
        if n <= 0 or k == 0 or start > 9:
            return
        for i in range(start, 10):
            cur.append(i)
            self.recur(res, cur, k - 1, n - i, i + 1)
            cur.pop()

if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))
