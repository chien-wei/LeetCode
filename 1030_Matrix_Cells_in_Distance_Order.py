class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # classic bfs question
        # use a 2d list to record visited cell that already push in result
        # having a list, usually it is queue, but here we can use it as result. 
        # To know where we are, keep an index.
        result = [[r0, c0]]
        visited = set()
        visited.add((r0, c0))
        i = 0
        while i < len(result):
            x, y = result[i]
            for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if a < 0 or a >= R or b < 0 or b >= C or (a, b) in visited:
                    continue
                visited.add((a,b))
                result.append([a, b])
            i += 1
        return result