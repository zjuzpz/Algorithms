"""
174. Dungeon Game
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""
# O(m * n)
# O(m + n)
class Solution(object):    
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 1
        m, n = len(dungeon), len(dungeon[0])
        lower_row = [max(-dungeon[-1][-1], 0)]
        for j in reversed(range(n - 1)):
            lower_row.append(max(lower_row[-1] - dungeon[m - 1][j], 0))
        right_row = [max(-dungeon[-1][-1], 0)]
        for i in reversed(range(m - 1)):
            right_row.append(max(0, right_row[-1] - dungeon[i][n - 1]))
        row = 1
        while row < m:
            cur_row = [right_row[row]]
            for j in range(1, n):
                cur_row.append(max(min(cur_row[-1], lower_row[j]) - dungeon[m - 1 - row][n - 1 - j] ,0))
            lower_row = cur_row
            row += 1
        return lower_row[-1] + 1

if __name__ == "__main__":
    d =[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(Solution().calculateMinimumHP(d))
