from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        # greedy
        used = defaultdict(lambda: 0)
        vl = list(zip(values, labels))
        vl.sort(key=lambda x: -x[0])
        res = 0
        i = 0
        while i < len(vl):
            v, l = vl[i]
            if used[l] != use_limit:
                res += v
                num_wanted -= 1
                used[l] += 1
                if num_wanted == 0:
                    return res
            i += 1
        return res