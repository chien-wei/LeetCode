from typing import List

class Solution:
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
print(s.findStrobogrammatic(1))
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(3))
print(s.findStrobogrammatic(4))
print(s.findStrobogrammatic(5))
