"""
317. Shortest Distance from All Buildings
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
# O(m * n * b)   b is the number of buildings
# O(m * n)
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dis = [[0 for j in range(n)] for i in range(m)]
        count = [[0 for j in range(n)] for i in range(m)]
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(dis, count, i, j, grid)
                    total += 1
        
        res = float("inf")
        for i in range(m):
            for j in range(n):
                if count[i][j] == total:
                    res = min(res, dis[i][j])
        
        if res == float("inf"):
            return -1
        return res
        
    def bfs(self, dis, count, x, y, grid):
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        visited[x][y] = True
        distance = 1
        stack = [(x, y)]
        while stack:
            next = []
            while stack:
                (x, y) = stack.pop()
                for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == 0:
                        next.append((i, j))
                        visited[i][j] = True
                        count[i][j] += 1
                        dis[i][j] += distance
            distance += 1
            stack = next

if __name__ == "__main__":
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    print(Solution().shortestDistance(grid))
