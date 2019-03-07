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


# 2019/03/06 update: 
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        tuple_for_sort = [(interval.start, interval.end, i, interval) for i, interval in enumerate(intervals)]
        tuple_for_sort.sort()
        sorted_intervals = list(map(lambda tuple2: tuple2[3], tuple_for_sort))
        
        res = []
        start, end = None, None
        for interval in sorted_intervals:
            if start == None:
                start = interval.start
                end = interval.end
                continue
            if interval.start > end:
                res.append([start, end])
                start = interval.start
                end = interval.end
            elif interval.start <= end:
                end = max(end, interval.end)
        if start != None:
            res.append([start, end])
        return res