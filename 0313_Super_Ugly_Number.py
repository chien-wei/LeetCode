# heap: TLE
from queue import PriorityQueue
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        primes.sort()
        pq = PriorityQueue()
        pq.put(1)
        prev = 0
        for _ in range(n-1):
            val = pq.get()
            while val == prev:
                val = pq.get()
            prev = val
            for prime in primes:
                nxt_val = prime * val
                pq.put(nxt_val)
        
        res = pq.get()
        while res == prev:
            res = pq.get()
        return res

# DP same as 0264: accepted
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]
        N = len(primes)
        idx = [0 for _ in range(N)]
        cands = [uglies[idx[i]] * primes[i] for i in range(N)]
        while n > 1:
            umin = min(cands)
            while umin == uglies[-1]:
                i = cands.index(umin)
                idx[i] += 1
                cands[i] = uglies[idx[i]] * primes[i]
                umin = min(cands)
            uglies.append(umin)
            n -= 1
        return uglies[-1]