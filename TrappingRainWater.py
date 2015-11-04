"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
# O(n)
# O(1)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        res = 0
        m = max(height)
        index = height.index(m)
        second = 0
        for i in range(index):
            if height[i] > second:
                second = height[i]
            else:
                res += second - height[i]
        second = 0
        j = len(height) - 1
        while j > index:
            if height[j] > second:
                second = height[j]
            else:
                res += second - height[j]
            j -= 1
        return res

if __name__ == "__main__":
    print(Solution().trap([3,1,5,4,1,2,3]))
