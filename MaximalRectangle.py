"""
85. Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing all ones and return its area.
"""
# O(m * n)
# O(n)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0 for j in range(n)]
        for j in range(n):
            if matrix[0][j] == "1":
                height[j] = 1
        res = self.helper(height)
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            res = max(res, self.helper(height))
        return res
    
    def helper(self, height):
        height = [-float("inf")] + height
        res, stack = 0, [0]
        for i in range(1, len(height)):
            while height[i] < height[stack[-1]]:
                index = stack.pop()
                width = i - stack[-1] - 1
                res = max(res, width * height[index])
            stack.append(i)
        right = stack[-1]
        while stack[-1] != 0:
            index = stack.pop()
            width = right - stack[-1]
            res = max(res, width * height[index])
        return res

if __name__ == "__main__":
    m = ["10", "10"]
    print(Solution().maximalRectangle(m))
