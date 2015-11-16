"""
118. Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
# O(n ^ 2)
# O(n)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res, i = [[1]], 1
        while i < numRows:
            tem, j = [], 0
            while j <= i:
                if j == 0 or j == i:
                    tem.append(1)
                else:
                    tem.append(res[-1][j - 1] + res[-1][j])
                j += 1
            res.append(tem)
            i += 1
        return res

if __name__ == "__main__":
    print(Solution().generate(5))
