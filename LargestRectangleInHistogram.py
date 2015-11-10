"""
84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""
# O(n)
# O(1)
class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.insert(0, float("-inf"))
        res, stack, area = 0, [0], 0
        for i in range(1, len(height)):
            while height[i] < height[stack[-1]]:
                tem = stack.pop()
                area = max(area, height[tem] * (i - stack[-1] - 1))
            stack.append(i)
        right = stack[-1]
        while stack[-1] != 0:
            tem = stack.pop()
            area = max(area, height[tem] * (right - stack[-1]))
        return area

if __name__ == "__main__":
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))
