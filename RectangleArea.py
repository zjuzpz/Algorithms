"""
223. Rectangle Area
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""
# O(1)
# O(1)
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        res = (C - A) * (D - B) + (G - E) * (H - F)
        if E < C and G > A and F < D and H > B:
            overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
            res -= overlap
        return res

if __name__ == "__main__":
    print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
