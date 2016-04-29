"""
63. Unique Path II
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""
# O(m * n)
# O(n)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [0 for i in range(n)]
        ways[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for j in range(1, n):
            ways[j] = ways[j - 1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                ways[0] = 0
            for j in range(1, n):
                ways[j] = ways[j] + ways[j - 1] if obstacleGrid[i][j] == 0 else 0
        return ways[-1]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
