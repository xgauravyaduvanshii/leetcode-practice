# LeetCode 3505. Minimum Operations to Make Elements Within K Subarrays Equal — Hard
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
# Submission 2202756748 — Accepted, Python3
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        # My thinking: the cheapest way to make one window of length x
        # all equal is to move every element to the window's median, so
        # I slide a window across the array keeping its median and the
        # cost of levelling it (two heaps, lower half and upper half,
        # with lazy deletion for the element sliding out). Then a
        # knapsack-style DP picks k non-overlapping windows: dp[i][j]
        # is the cheapest cost using j windows inside the first i
        # elements, either skipping position i or ending a window there.
        n = len(nums)
        lo = []  # max-heap (negated), lower half
        hi = []  # min-heap, upper half
        sum_lo = 0
        sum_hi = 0
        sz_lo = 0
        sz_hi = 0
        rem = defaultdict(int)

        def prune(heap, is_lo):
            while heap:
                v = -heap[0] if is_lo else heap[0]
                if rem[v] > 0:
                    rem[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal sum_lo, sum_hi, sz_lo, sz_hi
            prune(lo, True)
            prune(hi, False)
            while sz_lo > sz_hi + 1:
                v = -heapq.heappop(lo)
                sum_lo -= v
                sz_lo -= 1
                heapq.heappush(hi, v)
                sum_hi += v
                sz_hi += 1
                prune(lo, True)
            while sz_lo < sz_hi:
                v = heapq.heappop(hi)
                sum_hi -= v
                sz_hi -= 1
                heapq.heappush(lo, -v)
                sum_lo += v
                sz_lo += 1
                prune(hi, False)

        def add(v):
            nonlocal sum_lo, sum_hi, sz_lo, sz_hi
            prune(lo, True)
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v)
                sum_lo += v
                sz_lo += 1
            else:
                heapq.heappush(hi, v)
                sum_hi += v
                sz_hi += 1
            rebalance()

        def remove(v):
            nonlocal sum_lo, sum_hi, sz_lo, sz_hi
            prune(lo, True)
            prune(hi, False)
            rem[v] += 1
            if lo and v <= -lo[0]:
                sum_lo -= v
                sz_lo -= 1
            else:
                sum_hi -= v
                sz_hi -= 1
            prune(lo, True)
            prune(hi, False)
            rebalance()

        def window_cost():
            prune(lo, True)
            prune(hi, False)
            med = -lo[0]
            return med * sz_lo - sum_lo + sum_hi - med * sz_hi

        cost = [0] * n
        for i, v in enumerate(nums):
            add(v)
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                cost[i] = window_cost()
        INF = float("inf")
        dp_prev = [0] * (n + 1)
        for _ in range(k):
            dp_cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                dp_cur[i] = dp_cur[i - 1]
                if i >= x and dp_prev[i - x] < INF:
                    dp_cur[i] = min(dp_cur[i], dp_prev[i - x] + cost[i - 1])
            dp_prev = dp_cur
        return dp_prev[n]
