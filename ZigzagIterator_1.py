"""
281. Zigzag Iterator
Real zigzag iterator
v1 = [1, 2]
v2 = [3, 4, 5]
v3 = [6, 7]
return[1, 3, 6, 7, 4, 2, 5]
"""
# O(n)
# O(k)
class ZigzagIterator(object):

    def __init__(self, vs):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.stack1 = [(len(v), iter(v)) for v in reversed(vs) if v]
        self.stack2 = []
        self.forward = True

    def next(self):
        """
        :rtype: int
        """
        if self.forward:
            length, iter = self.stack1.pop()
            length -= 1
            if length:
                self.stack2.append((length, iter))
            if not self.stack1:
                self.forward = False
            return next(iter)
        length, iter = self.stack2.pop()
        length -= 1
        if length:
            self.stack1.append((length, iter))
        if not self.stack2:
            self.forward = True
        return next(iter)
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack1 or self.stack2 else False

if __name__ == "__main__":
    v1, v2, v3, v4, v5 = [1, 2], [3, 4, 5, 6], [], [8, 9], [10, 11, 12, 13, 14, 15]
    vs = [v1, v2, v3, v4, v5]
    i, v = ZigzagIterator(vs), []
    while i.hasNext():
        num = i.next()
        v.append(num)
    print(v)
