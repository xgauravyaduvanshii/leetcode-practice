import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # My thinking: always take the richest project I can afford —
        # sweep projects by required capital into a max-heap of
        # profits, and repeat k times.
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w
