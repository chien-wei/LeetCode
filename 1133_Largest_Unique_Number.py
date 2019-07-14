from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        count = defaultdict(lambda: 0)
        for a in A:
            count[a] += 1
        ans = -1
        for num in count:
            if count[num] == 1:
                ans = max(ans, num)
        return ans