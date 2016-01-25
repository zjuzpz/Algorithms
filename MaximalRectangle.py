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
        stack, res = [0 for i in range(len(matrix[0]))], 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    stack[j] += 1
                else:
                    stack[j] = 0
            res = max(res, self.helper(stack))
        return res
        
    def helper(self, h):
        height = h[:]
        height.insert(0, 0)
        res, stack = 0, []
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                index = stack.pop()
                res = max(res, (i - stack[-1] - 1) * height[index])
            stack.append(i)
        last = len(height)
        while len(stack) > 1:
            index = stack.pop()
            res = max(res, (last - stack[-1] - 1) * height[index])
        return res

if __name__ == "__main__":
    m = ["10", "10"]
    print(Solution().maximalRectangle(m))
