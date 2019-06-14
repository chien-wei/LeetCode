class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # the first t is the time require to finish the course
        # we always don't like the course that take most time
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda x: x[1]):
            start += t
            print(t, end, start)
            heapq.heappush(pq, -t)
            if start > end:
                start += heapq.heappop(pq)
        return len(pq)