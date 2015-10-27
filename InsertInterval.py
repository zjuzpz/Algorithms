"""
57. Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
# O(n)
# O(1)
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}->{}]".format(self.start, self.end)

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res, i, index = [], 0, None
        while i < len(intervals):
            if intervals[i].start > newInterval.end:
                res.append(newInterval)
                res += intervals[i:]
                return res
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
            i += 1
        res.append(newInterval)
        return res

if __name__ == "__main__":
    intervals = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
    print(Solution().insert(intervals, Interval(4, 9)))
