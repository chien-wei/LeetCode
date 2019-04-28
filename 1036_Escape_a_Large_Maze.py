class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # BFS
        bound = 10 ** 6
        step_left = len(blocked)
        que = [source]
        visited = set(tuple(source))
        blocked = set(map(tuple, blocked))
        
        while len(que) > 0 and step_left >= 0:
            for _ in range(len(que)):
                i, j = que.pop(0)
                for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if x >= 0 and x < bound and y >= 0 and y < bound and (x, y) not in blocked and (x, y) not in visited:
                        if [x, y] == target:
                            return True
                        que.append((x, y))
                        visited.add((x, y))
            step_left -= 1
        if step_left <= 0:
            return True
        return False