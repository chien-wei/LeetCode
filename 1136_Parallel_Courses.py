from collections import defaultdict
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        # For each semester, take those classes with 0 degree
        # Store graph information with dict
        degrees = [0 for _ in range(N+1)]
        prereqs = defaultdict(list)
        for a, b in relations:
            degrees[b] += 1
            prereqs[a].append(b)
        
        ans = 0 # num of semesters
        numOfZeroDegree = degrees[1:].count(0)
        numOfVisited = 0
        
        while numOfZeroDegree != 0:
            numOfVisited += numOfZeroDegree
            nextDegrees = degrees[:]
            for i in range(1, N+1):
                if degrees[i] == 0:
                    nextDegrees[i] = -1
                    for j in prereqs[i]:
                        nextDegrees[j] -= 1
            ans += 1
            degrees = nextDegrees
            numOfZeroDegree = degrees[1:].count(0)
        return ans if numOfVisited == N else -1