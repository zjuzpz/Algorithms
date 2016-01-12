"""
311. Sparse Matrix Multiplication
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
# O(l * m　* n)
# O(l * m)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []
        res = [[0 for j in range(len(B[0]))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    for k in range(len(res[0])):
                        res[i][k] += A[i][j] * B[j][k]
        return res

if __name__ == "__main__":
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(Solution().multiply(A, B))
