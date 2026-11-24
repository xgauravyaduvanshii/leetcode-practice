# LeetCode 3594. Minimum Time to Transport All Individuals — Hard
# https://leetcode.com/problems/minimum-time-to-transport-all-individuals/
# Submission 2202865008 — Accepted, Python3
import heapq
import itertools
from typing import List


class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        # My thinking: the whole situation is which people are
        # already across, which stage we are in, and which side the
        # boat is on — that is the full state. From a state I either
        # send a group of up to k people across (the crossing takes
        # the slowest member's time times the stage multiplier) or
        # send one person back, and the stage advances by the whole
        # minutes of the trip, modulo m. Dijkstra over that state
        # space gives the cheapest way to get everyone across; if
        # the boat can only carry one person at a time and there are
        # two or more people, nobody can ever finish, so it is -1.
        FULL = (1 << n) - 1
        INF = float("inf")
        dist = {}
        start = (0, 0, False)
        dist[start] = 0.0
        pq = [(0.0, 0, 0, False)]
        while pq:
            d, mask, stage, boat = heapq.heappop(pq)
            if d > dist.get((mask, stage, boat), INF) + 1e-9:
                continue
            if mask == FULL:
                return d
            if not boat:
                base = [i for i in range(n) if not (mask >> i) & 1]
                for r in range(1, min(k, len(base)) + 1):
                    for combo in itertools.combinations(base, r):
                        mx = max(time[i] for i in combo)
                        cross = mx * mul[stage]
                        ns = (stage + int(cross // 1)) % m
                        nmask = mask
                        for i in combo:
                            nmask |= 1 << i
                        nd = d + cross
                        key = (nmask, ns, True)
                        if nd < dist.get(key, INF) - 1e-9:
                            dist[key] = nd
                            heapq.heappush(pq, (nd, nmask, ns, True))
            else:
                dest = [i for i in range(n) if (mask >> i) & 1]
                for r in dest:
                    ret = time[r] * mul[stage]
                    ns = (stage + int(ret // 1)) % m
                    nmask = mask & ~(1 << r)
                    nd = d + ret
                    key = (nmask, ns, False)
                    if nd < dist.get(key, INF) - 1e-9:
                        dist[key] = nd
                        heapq.heappush(pq, (nd, nmask, ns, False))
        return -1.0
