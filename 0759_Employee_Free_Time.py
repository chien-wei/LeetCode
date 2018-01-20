# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from itertools import chain

class Solution:
    def employeeFreeTime(self, avails):
        """
        :type avails: List[List[Interval]]
        :rtype: List[Interval]
        """
        avails = list(sorted(chain(*avails), key=lambda interval: interval.start))
        
        start, end = [avails[0].start, avails[0].end]
        result = []
        for i in avails[1:]:
            if i.start <= end:
                end = max(end, i.end)
            elif i.start > end:
                result.append([end, i.start])
                start = i.start
                end = i.end
            
                
        return result