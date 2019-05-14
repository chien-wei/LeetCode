# Accepted: using heap
import queue
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = {}
        mn = queue.PriorityQueue()
        if n < 1:
            return 0
        mn.put(2)
        mn.put(3)
        mn.put(5)
        sm = 1
        for _ in range(n-1):
            sm = mn.get()
            if sm * 2 not in seen:
                mn.put(sm * 2)
                seen[sm * 2] = True
            if sm * 3 not in seen:
                mn.put(sm * 3)
                seen[sm * 3] = True
            if sm * 5 not in seen:
                mn.put(sm * 5)
                seen[sm * 5] = True
        return sm

# Accepted: three pointer
import queue
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]