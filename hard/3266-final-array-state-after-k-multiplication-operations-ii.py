# LeetCode 3266. Final Array State After K Multiplication Operations II — Hard
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/
# Submission 2202160109 — Accepted, Python3
#
# My thinking: always multiply the smallest
# element, which a heap gives in order. Once
# the smallest times the multiplier passes the
# current maximum, the heap order stops changing
# — the remaining k operations just cycle through
# all n elements evenly. So I simulate only until
# that point, then hand out the leftover
# multiplications round-robin with fast modular
# powers instead of simulating them one by one.

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        import heapq
        MOD = 10 ** 9 + 7
        if multiplier == 1:
            return [x % MOD for x in nums]
        n = len(nums)
        cur = list(nums)
        max_v = max(cur)
        heap = [(cur[i], i) for i in range(n)]
        heapq.heapify(heap)
        while k > 0:
            v, i = heap[0]
            if v * multiplier > max_v:
                break
            heapq.heappop(heap)
            v *= multiplier
            cur[i] = v
            heapq.heappush(heap, (v, i))
            k -= 1
        if k == 0:
            return [x % MOD for x in cur]
        order = sorted(heap)
        q, r = divmod(k, n)
        extra = [0] * n
        for rank, (v, i) in enumerate(order):
            extra[i] = q + (1 if rank < r else 0)
        return [(cur[i] % MOD) * pow(multiplier, extra[i], MOD) % MOD for i in range(n)]
