class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        max_ab = max(0, b - a - 1)
        max_bc = max(0, c - b - 1)
        if max_ab == 0 and max_bc == 0:
            return [0, 0]
        elif max_ab == 0 or max_bc == 0:
            return [1, max_ab + max_bc]
        else:
            return [min(max_ab, max_bc, 2), max_ab + max_bc]