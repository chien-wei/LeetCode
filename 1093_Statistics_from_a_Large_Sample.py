# statistics: TLE
from statistics import median, mean, mode
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # minimum, maximum, mean, median, and mode
        li = []
        for i in range(256):
            li = li + [i] * count[i]
        return [float(min(li)), float(max(li)), mean(li), float(median(li)), float(mode(li))]

# O(n) Solution: Accepted
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mn = mx = mode = mean = median = -1
        most_count = 0
        _sum = 0
        _count = 0
        for i in range(256):
            if mn == -1 and count[i] != 0:
                mn = i
            if count[i] != 0:
                mx = i
                _sum += i * count[i]
                _count += count[i]
            if count[i] > most_count:
                mode = i
                most_count = count[i]
        half = _count // 2
        for i in range(256):
            if half > 0:
                half -= count[i]
            if half == 0 and half % 2 == 0:
                median = (i + i+1) / 2
                break
            elif half < 0:
                median = float(i)
                break
                
        return [float(mn), float(mx), _sum / _count, median, float(mode)]