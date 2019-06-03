class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # first sort the intervals
        # pick the last two element, which have more possibility to cover the next interval
        res = []
        intervals.sort(key=lambda x: x[1])
        for start, end in intervals:
            if len(res) == 0 or res[-1] < start:
                res.append(end - 1)
                res.append(end)
            elif res[-2] < start:
                res.append(end)
        return len(res)