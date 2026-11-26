# LeetCode 4086. Minimum Interval Selection to Cover Target Intervals — Hard
# https://leetcode.com/problems/minimum-interval-selection-to-cover-target-intervals/
# Submission 2203703374 — Accepted, Python3
import heapq
from typing import List


class Solution:
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:
        # My thinking: first merge the target intervals (sorted, so
        # overlapping or touching targets join into one segment to
        # cover), then cover each merged segment greedily from left
        # to right. At the leftmost uncovered point, push every
        # available interval that starts at or before it into a
        # max-heap keyed by right end, and always take the one that
        # reaches furthest — the classic minimum-interval-cover
        # greedy, which is optimal because any cover of the point
        # must use an interval starting at or before it, and the
        # furthest-reaching one can only help later segments. If
        # the heap is empty, or the best interval ends before the
        # point, the segment cannot be covered, so return -1.
        # Point-interval edge case: an available interval ending
        # exactly at the uncovered point still covers it when that
        # point is the segment's right end — e.g. available [2,2]
        # covers target [2,2], because the loop stops once reach
        # equals r, and the interval is counted once.
        targetIntervals.sort()
        merged = []
        for l, r in targetIntervals:
            if merged and l <= merged[-1][1]:
                if r > merged[-1][1]:
                    merged[-1][1] = r
            else:
                merged.append([l, r])
        availableIntervals.sort(key=lambda x: x[0])
        heap = []
        i = 0
        n = len(availableIntervals)
        reach = None
        count = 0
        for l, r in merged:
            point = l if reach is None or reach < l else reach
            while reach is None or reach < r:
                while i < n and availableIntervals[i][0] <= point:
                    heapq.heappush(heap, -availableIntervals[i][1])
                    i += 1
                if not heap:
                    return -1
                best = -heapq.heappop(heap)
                if best < point:
                    return -1
                reach = best
                count += 1
                point = reach
        return count
