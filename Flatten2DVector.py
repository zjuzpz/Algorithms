"""
251. Flatten 2D Vector
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,2,3,4,5,6].
"""
# O(1)
# O(1)
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.row = 0
        self.col = 0

    def next(self):
        """
        :rtype: int
        """
        tem = self.vec[self.row][self.col]
        self.col += 1
        return tem

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.vec:
            return False
        while self.col >= len(self.vec[self.row]):
            self.col = 0
            self.row += 1
            if self.row >= len(self.vec):
                return False
        return True

if __name__ == "__main__":
    vec2d = [[1, 2], [], [3], [4, 5, 6], []]
    i, v = Vector2D(vec2d), []
    while i.hasNext():
        v.append(i.next())
    print(v)
