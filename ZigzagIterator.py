"""
281. Zigzag Iterator
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
"""
# O(n)
# O(1) no extra space
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v, self.cur = [], 0
        for i in range(min(len(v1), len(v2))):
            self.v.append(v1[i])
            self.v.append(v2[i])
        if len(v1) < len(v2):
            self.v.extend(v2[len(v1) :])
        if len(v1) > len(v2):
            self.v.extend(v1[len(v2) :])

    def next(self):
        """
        :rtype: int
        """
        tem = self.v[self.cur]
        self.cur += 1
        return tem

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur < len(self.v)

if __name__ == "__main__":
    v1, v2 = [1, 2], [3, 4, 5, 6]
    i, v = ZigzagIterator(v1, v2), []
    while i.hasNext(): v.append(i.next())
    print(v)
