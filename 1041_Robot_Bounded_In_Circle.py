class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        DIR = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        pos = [0, 0]
        di = 0
        for i in range(100):
            for c in instructions:
                if c == "G":
                    pos = list(map(lambda x, y: x+y, pos, DIR[di]))
                elif c == "L":
                    di = (di + 4 - 1) % 4
                elif c == "R":
                    di = (di + 1) % 4
            if pos == [0, 0]:
                return True
        return False