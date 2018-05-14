# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 1:
            return []
        intervals.sort(key=lambda x: x.start)
        ans = [intervals.pop(0)]
        for i in intervals:
            if ans[-1].end >= i.start:
                ans[-1].end = max(ans[-1].end, i.end)
            else:
                ans.append(i)
        return ans