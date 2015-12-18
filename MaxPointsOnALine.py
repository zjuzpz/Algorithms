"""
149. Max Points on a Line
Given n points on a 2D plane,
find the maximum number of points that lie on the same straight line.
"""
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

# O(n ^ 2)
# O(n)
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            same_points, tem_res, lookup = 1, 0, {}
            lookup["inf"] = 0
            for j in range(i + 1, len(points)):
                if (points[j].x, points[j].y) == (points[i].x, points[i].y):
                    same_points += 1
                elif points[j].x == points[i].x:
                    lookup["inf"] += 1
                    tem_res = max(tem_res, lookup["inf"])
                else:
                    k = (points[j].y - points[i].y) * 1.0 / (points[j].x - points[i].x)
                    if k not in lookup:
                        lookup[k] = 0
                    lookup[k] += 1
                    tem_res = max(tem_res, lookup[k])
            res = max(res, tem_res + same_points)
        return res

if __name__ == "__main__":
    points = [Point(0, 0), Point(1, 1), Point(0, 0), Point(1, 3), Point(2, 2)]
    print(Solution().maxPoints(points))
