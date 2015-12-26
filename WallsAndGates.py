"""
286. Walls and Gates
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
# O(m * n)
# O(g)
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        distance = 1
        stack = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    stack.append((i, j))
        while stack:
            next_turn = []
            while stack:
                (i, j) = stack.pop()
                if i > 0 and rooms[i - 1][j] == 2 ** 31 - 1:
                    rooms[i - 1][j] = distance
                    next_turn.append((i - 1, j))
                if i < len(rooms) - 1 and rooms[i + 1][j] == 2 ** 31 - 1:
                    rooms[i + 1][j] = distance
                    next_turn.append((i + 1, j))
                if j > 0 and rooms[i][j - 1] == 2 ** 31 - 1:
                    rooms[i][j - 1] = distance
                    next_turn.append((i, j - 1))
                if j < len(rooms[0]) - 1 and rooms[i][j + 1] == 2 ** 31 - 1:
                    rooms[i][j + 1] = distance
                    next_turn.append((i, j + 1))
            distance += 1
            stack = next_turn

if __name__ == "__main__":
    INF = 2 ** 31 - 1
    rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], \
             [INF, -1, INF, -1], [0, -1, INF, INF]]
    Solution().wallsAndGates(rooms)
    print(rooms)
