"""
305. Number of Islands II
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""
# O(klog*k)
# O(k)
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        lookup, res, count = {}, [], 0
        for position in positions:
            (x, y) = position
            id = x * n + y
            lookup[id] = id
            count += 1
            for (i, j) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= i < m and 0 <= j < n:
                    neighbo_id = i * n + j
                    if neighbo_id in lookup and self.find_root(lookup, neighbo_id) != self.find_root(lookup, id):
                        count -= 1
                        self.union(lookup, neighbo_id, id)
            res.append(count)
        return res
        
    def find_root(self, lookup, id):
        if lookup[id] == id:
            return id
        return self.find_root(lookup, lookup[id])
        
    def union(self, lookup, n1, n2):
        root1, root2 = self.find_root(lookup, n1), self.find_root(lookup, n2)
        lookup[min(root1, root2)] = max(root1, root2)
        
if __name__ == "__main__":
    positions = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
    print(Solution().numIslands2(3, 3, positions))
