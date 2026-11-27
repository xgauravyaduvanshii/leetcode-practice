import heapq


class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        # My thinking: take the engineers in efficiency order —
        # the current engineer's efficiency is the team's, so
        # keep the k fastest speeds seen so far and multiply.
        MOD = 10 ** 9 + 7
        order = sorted(range(n), key=lambda i: -efficiency[i])
        heap = []
        speed_sum = 0
        best = 0
        for i in order:
            heapq.heappush(heap, speed[i])
            speed_sum += speed[i]
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            best = max(best, speed_sum * efficiency[i])
        return best % MOD
