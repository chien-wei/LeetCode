from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # times: List[List[s, t, dist]]
        # dijkstra's and remember to keep track of time
        dic = defaultdict(list) # {2: (1, 1), (1, 3), 3: (1, 4)}
        for s, t, time in times:
            dic[s].append((time, t))
        
        visited = [False for _ in range(N+1)]
        visited[0] = True
        curTime = 0
        heap = []
        heappush(heap, (0, K))
        while len(heap) > 0:
            time, t = heappop(heap)
            if visited[t]:
                continue
            visited[t] = True
            curTime = max(curTime, time)
            for time2, t2 in dic[t]:
                heappush(heap, (time2 + time, t2))
        
        return curTime if all(visited) else -1