# LeetCode 1851. Minimum Interval to Include Each Query — Hard
# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Submission 2201199754 — Accepted, Python3
#
# My thinking: I sort the intervals by their left
# end and sweep the queries in order, keeping the
# intervals that have started in a heap by size
# and dropping the ones that already ended — the
# smallest one left is the answer.

import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> int:
        intervals.sort(key=lambda x: x[0])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [-1] * len(queries)
        heap = []
        j = 0
        for qi in order:
            q = queries[qi]
            while j < len(intervals) and intervals[j][0] <= q:
                l, r = intervals[j]
                heapq.heappush(heap, (r - l + 1, r))
                j += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                ans[qi] = heap[0][0]
        return ans
