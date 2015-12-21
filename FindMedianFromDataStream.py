"""
295. Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2
"""
# O(logn)
# O(1)
from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.max_heap or num > -self.max_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        return self.min_heap[0]


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(3)
    mf.addNum(2)
    print(mf.findMedian())
