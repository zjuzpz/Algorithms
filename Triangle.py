"""
120. Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
# O(n)
# O(l)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        t = triangle
        if not t:
            return 0
        res = t[0]
        for i in range(1, len(t)):
            tem = []
            for j in range(len(t[i])):
                if j == 0:
                    tem.append(res[0] + t[i][0])
                elif j == len(t[i]) - 1:
                    tem.append(res[-1] + t[i][-1])
                else:
                    tem.append(min(res[j - 1], res[j]) + t[i][j])
            res = tem
        return min(res)

if __name__ == "__main__":
    t = [[-1], [2,3], [1,-1,-3]]
    print(Solution().minimumTotal(t))
