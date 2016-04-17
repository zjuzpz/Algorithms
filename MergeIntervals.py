"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# O(nlogn)
# O(1)
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{},{}]".format(self.start,self.end)
        
        
from copy import copy
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key = lambda x: x.start)
        res, new = [], copy(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i].start > new.end:
                res.append(new)
                new = copy(intervals[i])
            else:
                new.end = max(new.end, intervals[i].end)
        res.append(new)
        return res

if __name__ == "__main__":
    intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    print(Solution().merge(intervals))
    for interval in intervals:
        print(interval, end = ",")
