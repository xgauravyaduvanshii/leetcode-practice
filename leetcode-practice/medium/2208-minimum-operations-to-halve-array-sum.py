# LeetCode 2208. Minimum Operations to Halve Array Sum — Medium
# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
# Submission 2204500136 — Accepted, Python3
#
# My thinking: halving the largest element removes the most from the
# sum, so I always halve the current maximum — a max-heap gives it to
# me in order. I repeat until the running sum drops to at most half of
# the original, counting each halving.
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        import heapq
        heap = [-float(x) for x in nums]
        heapq.heapify(heap)
        total = sum(nums)
        target = total / 2
        cur = float(total)
        ops = 0
        while cur > target:
            largest = -heapq.heappop(heap)
            halved = largest / 2
            cur -= largest - halved
            heapq.heappush(heap, -halved)
            ops += 1
        return ops
