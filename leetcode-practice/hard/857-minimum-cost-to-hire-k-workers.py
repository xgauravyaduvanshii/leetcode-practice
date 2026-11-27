import heapq
from fractions import Fraction


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        # My thinking: the group's pay is set by its highest
        # wage-per-quality ratio, so try each worker as that cap and
        # keep the k cheapest qualities under it.
        workers = sorted(
            (Fraction(w, q), q) for q, w in zip(quality, wage)
        )
        max_heap = []
        quality_sum = 0
        best = None
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            quality_sum += q
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)
            if len(max_heap) == k:
                cost = ratio * quality_sum
                best = cost if best is None else min(best, cost)
        return float(best)
