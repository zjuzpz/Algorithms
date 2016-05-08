"""
346. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
# O(1)
# O(k)
from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = deque()
        self.size = size
        self.total = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if not self.nums:
            self.nums.append(val)
            return val
        if len(self.nums) == self.size:
            self.total -= self.nums.popleft()
        self.total += val
        self.nums.append(val)
        return self.total / len(self.nums) * 1.0
        
if __name__ == "__main__":
    m = MovingAverage(3)
    print(m.next(1))
    print(m.next(10))
    print(m.next(3))
    print(m.next(5))
