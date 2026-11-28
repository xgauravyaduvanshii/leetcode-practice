# LeetCode 2530. Maximal Score After Applying K Operations — Medium
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/
# Submission 2205051089 — Accepted, Python3
#
# My thinking: each operation should take the current largest
# element, so keep a max-heap (negated values). After taking x,
# it comes back as ceil(x / 3), which is (x + 2) // 3.
import heapq


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            x = -heapq.heappop(heap)
            score += x
            heapq.heappush(heap, -((x + 2) // 3))
        return score
