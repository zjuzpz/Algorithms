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
        
        
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x: x.start)
        i = 1
        while i < len(intervals):
            if intervals[i].start > intervals[i - 1].end:
                i += 1
            else:
                new = Interval(intervals[i - 1].start, max(intervals[i - 1].end, intervals[i].end))
                intervals[i - 1] = new
# Note here del function may be expensive, thus we can create a new list to store the result
                del intervals[i]
        return intervals

if __name__ == "__main__":
    intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    print(Solution().merge(intervals))
