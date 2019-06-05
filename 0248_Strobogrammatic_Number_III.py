# need optimized
from typing import List

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> List[str]:
        dl, dh = len(low), len(high)
        res = []
        for i in range(dl, dh+1):
            for s in self.findStrobogrammatic(i):
                print(s)
                if int(s) > int(low) and int(s) < int(high):
                    res.append(s)
        return res
    
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.SIDES = [("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
        self.flatten = lambda z: [x for y in z for x in y]

        def loop(n: int) -> List[str]:
            if n < 0:
                return []
            if n == 0:
                return [""]
            elif n == 1:
                return ["0", "1", "8"]
            else:
                return list(self.flatten( \
                    map(lambda s: [head + s + tail for head, tail in self.SIDES], \
                    loop(n-2) + list(map(lambda t: "0" + t + "0", loop(n-4))))))

        return loop(n)

s = Solution()
print(s.strobogrammaticInRange("50", "100"))
