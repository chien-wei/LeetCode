from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # just another way to ask maximum overlap intervals
        # track number of room used by time
        dic = {}

        for s, e in intervals:
            dic[s] = dic.get(s, 0) + 1
            dic[e] = dic.get(e, 0) - 1
        
        res = 0
        using = 0
        for t in sorted(dic.keys()):
            using += dic[t]
            res = max(res, using)
        return res
s = Solution()
print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(s.minMeetingRooms([[2,15],[36,45],[9,29],[16,23],[4,9]]))
print(s.minMeetingRooms([[928,5032],[3072,3741],[3960,4588],[482,2269],[2030,4360],[150,772]]))
print(s.minMeetingRooms([[9,50],[30,37],[39,45],[4,22],[20,43],[1,7]]))
print(s.minMeetingRooms([[9,50],[30,37],[20,43],[1,7]]))
