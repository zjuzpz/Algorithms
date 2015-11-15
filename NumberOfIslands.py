"""
200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
# O(m * n)
# O(m * n)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        res, visited = 0, [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    visited[i][j] = True
                    self.DFS(i, j, visited, grid)
        return res
        
    def DFS(self, i, j, visited, grid):
        if i - 1 >= 0 and grid[i - 1][j] == "1" and not visited[i - 1][j]:
            visited[i - 1][j] = True
            self.DFS(i - 1, j, visited, grid)
        if i + 1 < len(grid) and grid[i + 1][j] == "1" and not visited[i + 1][j]:
            visited[i + 1][j] = True
            self.DFS(i + 1, j, visited, grid)
        if j - 1 >= 0 and grid[i][j - 1] == "1" and not visited[i][j - 1]:
            visited[i][j - 1] = True
            self.DFS(i, j - 1, visited, grid)
        if j + 1 < len(grid[0]) and grid[i][j + 1] == "1" and not visited[i][j + 1]:
            visited[i][j + 1] = True
            self.DFS(i, j + 1, visited, grid)

if __name__ == "__main__":
    grid = ["11000","11000","00100","00011"]
    print(Solution().numIslands(grid))
