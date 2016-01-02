"""
296. Best Meeting Point
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.
"""
# O(nlogn)
# O(n)
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        return self.getMin(row) + self.getMin(col)
        
    def getMin(self, dis):
        dis.sort()
        i, j, res = 0, len(dis) - 1, 0
        while i < j:
            res += (dis[j] - dis[i])
            i, j = i + 1, j - 1
        return res 

# O(n)
# O(n)
import random
class Solution2(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        return self.getMin(row) + self.getMin(col)
        
    def getMin(self, dis):
        mid = self.quickSelect(dis, len(dis) // 2 + 1)
        res = 0
        for i in dis:
            res += abs(i - mid)
        return res
        
    def quickSelect(self, num, k):
        lower, upper = 0, len(num) - 1
        while lower <= upper:
            pivot = random.randint(lower, upper)
            new_pivot = self.partition(num, pivot, lower, upper)
            if new_pivot == k - 1:
                return num[new_pivot]
            if new_pivot < k - 1:
                lower = new_pivot + 1
            else:
                upper = new_pivot - 1
                
    def partition(self, num, pivot, lower, upper):
        pivot_val, new_pivot = num[pivot], lower
        num[upper], num[pivot] = num[pivot], num[upper]
        for i in range(lower, upper):
            if num[i] <= pivot_val:
                num[i], num[new_pivot] = num[new_pivot], num[i]
                new_pivot += 1
        num[new_pivot], num[upper] = num[upper], num[new_pivot]
        return new_pivot



if __name__ == "__main__":
    grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    print(Solution2().minTotalDistance(grid))
