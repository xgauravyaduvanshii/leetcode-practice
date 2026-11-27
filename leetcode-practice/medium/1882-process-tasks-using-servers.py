import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # My thinking: keep two heaps — the free servers by
        # weight, and the busy ones by when they finish — so
        # each task goes to the lightest server that is free,
        # waiting if none is.
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        busy = []
        answer = []
        time = 0
        for j, duration in enumerate(tasks):
            time = max(time, j)
            while busy and busy[0][0] <= time:
                free_time, w, i = heapq.heappop(busy)
                heapq.heappush(available, (w, i))
            if not available:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    free_time, w, i = heapq.heappop(busy)
                    heapq.heappush(available, (w, i))
            w, i = heapq.heappop(available)
            answer.append(i)
            heapq.heappush(busy, (time + duration, w, i))
        return answer
