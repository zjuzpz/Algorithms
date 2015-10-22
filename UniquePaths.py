"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
"""
# DP
# O(n * m)
# O(n * m)
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        if m <= 1 or n<= 1:
            return 1
        matrix = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            matrix[0][i] = 1
        for i in range(m):
            matrix[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]
    
# O(n * m)
# O(m + n)    
class Solution2:
    # @return an integer
    def uniquePaths(self, m, n):
        if m < n:
            return self.uniquePaths(n, m)
        ways = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                ways[j] += ways[j - 1]
        
        return ways[n - 1]

# math
# O(m)
# O(1)   
class Solution3(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.uniquePaths(n, m)
        num = m + n - 2
        i, res = 0, 1
        while i < m - 1:
            res *= (num - i)
            i += 1
        i = 1
        while i < m - 1:
            res //= (m - i)
            i += 1
        return res

if __name__ == "__main__":
    print(Solution3().uniquePaths(1000,1000))
