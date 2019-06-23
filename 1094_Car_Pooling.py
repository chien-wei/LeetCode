class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # same as Meeting Room II
        dic = {}
        for val, s, e in trips:
            dic[s] = dic.get(s, 0) + val
            dic[e] = dic.get(e, 0) - val
        
        res = 0
        using = 0
        for t in sorted(dic.keys()):
            using += dic[t]
            res = max(res, using)
        return res <= capacity