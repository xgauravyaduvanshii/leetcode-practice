import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        # My thinking: first double every odd number so all
        # are even — then keep halving the biggest one while
        # it stays even and watch the spread shrink.
        heap = []
        cur_min = float("inf")
        for x in nums:
            if x % 2 == 1:
                x *= 2
            heapq.heappush(heap, -x)
            cur_min = min(cur_min, x)
        best = -heap[0] - cur_min
        while -heap[0] % 2 == 0:
            x = -heapq.heappop(heap)
            x //= 2
            cur_min = min(cur_min, x)
            heapq.heappush(heap, -x)
            best = min(best, -heap[0] - cur_min)
        return best
