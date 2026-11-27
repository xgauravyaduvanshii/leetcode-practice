import heapq


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        # My thinking: take courses in deadline order, and whenever
        # the total runs past a deadline, drop the longest course
        # taken so far — the heap always holds the best set.
        courses.sort(key=lambda c: c[1])
        max_heap = []
        total = 0
        for duration, deadline in courses:
            heapq.heappush(max_heap, -duration)
            total += duration
            if total > deadline:
                total += heapq.heappop(max_heap)
        return len(max_heap)
