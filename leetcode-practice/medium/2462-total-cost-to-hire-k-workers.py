# LeetCode 2462. Total Cost to Hire K Workers — Medium
# https://leetcode.com/problems/total-cost-to-hire-k-workers/
# Submission 2200988832 — Accepted, Python3
#
# My thinking: I keep two heaps for the cheapest workers
# at each end, hire the cheaper of the two fronts, and
# refill from the middle as the ends move inward.

import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        left = costs[:candidates]
        right = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(left)
        heapq.heapify(right)
        i, j = candidates, len(costs) - candidates - 1
        total = 0
        for _ in range(k):
            if not right or (left and left[0] <= right[0]):
                total += heapq.heappop(left)
                if i <= j:
                    heapq.heappush(left, costs[i])
                    i += 1
            else:
                total += heapq.heappop(right)
                if i <= j:
                    heapq.heappush(right, costs[j])
                    j -= 1
        return total
