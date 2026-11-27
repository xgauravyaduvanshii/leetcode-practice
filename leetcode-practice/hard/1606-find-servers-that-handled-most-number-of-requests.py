import bisect
import heapq


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # My thinking: each request wants its turn's server or
        # the next free one clockwise — so keep the free servers
        # sorted and the busy ones in a heap by finish time.
        free = list(range(k))
        busy = []
        handled = [0] * k
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, sid = heapq.heappop(busy)
                bisect.insort(free, sid)
            if not free:
                continue
            want = i % k
            pos = bisect.bisect_left(free, want)
            if pos == len(free):
                pos = 0
            sid = free.pop(pos)
            handled[sid] += 1
            heapq.heappush(busy, (t + d, sid))
        most = max(handled)
        return [i for i, c in enumerate(handled) if c == most]
