"""
302. Smallest Rectangle Enclosing Black Pixels
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
"""
# O(nlogn)
# O(1)
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        left = self.binarySearch(0, y, lambda x : any(row[x] == "1" for row in image))
        right = self.binarySearch(y + 1, len(image[0]), lambda x: all(row[x] == "0" for row in image))
        top = self.binarySearch(0, x, lambda x: "1" in image[x])
        bottom = self.binarySearch(x + 1, len(image), lambda x: "1" not in image[x])
        return (right - left) * (bottom - top)
        
    def binarySearch(self, lower, upper, check):
        while lower < upper:
            mid = (lower + upper) // 2
            if check(mid):
                upper = mid
            else:
                lower = mid + 1
        return lower

if __name__ == "__main__":
    image = [
  "0010",
  "0110",
  "0100"
]
    print(Solution().minArea(image, 0, 2))
