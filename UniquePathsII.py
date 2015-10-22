"""
63. Unique Path II
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""
# O(m * n)
# O(m * n)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        g = obstacleGrid
        if not g or g[0][0] == 1:
            return 0
        m, n = len(g), len(g[0])
        g[0][0] = 1
        i, j = 1, 1
        while j < n:
            if g[0][j] == 0:
                g[0][j] = 1
            else:
                while j < n:
                    g[0][j] = 'X'
                    j += 1
            j += 1
        while i < m:
            if g[i][0] == 0:
                g[i][0] = 1
            else:
                while i < m:
                    g[i][0] = 'X'
                    i += 1
            i += 1
        for i in range(1, m):
            for j in range(1, n):
                if g[i][j] == 0:
                    if g[i - 1][j] == g[i][j - 1] == 'X':
                        g[i][j] = 'X'
                    elif g[i - 1][j] == 'X':
                        g[i][j] = g[i][j - 1]
                    elif g[i][j - 1] == 'X':
                        g[i][j] = g[i - 1][j]
                    else:
                        g[i][j] = g[i - 1][j] + g[i][j - 1]
                else:
                    g[i][j] = 'X'
        if g[-1][-1] == 'X':
            return 0
        return g[-1][-1]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
