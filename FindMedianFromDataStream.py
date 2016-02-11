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
from heapq import heappush
from heapq import heappop

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.maxHeap or num > -self.maxHeap[0]:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heappush(self.maxHeap, -heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        return self.minHeap[0] * 1.0

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(3)
    mf.addNum(2)
    print(mf.findMedian())
