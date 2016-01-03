"""
253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# O(nlogn)
# O(n)
from heapq import heappush
from heapq import heappop
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda interval : interval.start)
        time = []
        for interval in intervals:
            if time and time[0] <= interval.start:
                heappop(time)
            heappush(time, interval.end)
        return len(time)

if __name__ == "__main__":
    intervals = [Interval(15, 20), Interval(0, 30), Interval(5, 10)]
    print(Solution().minMeetingRooms(intervals))
