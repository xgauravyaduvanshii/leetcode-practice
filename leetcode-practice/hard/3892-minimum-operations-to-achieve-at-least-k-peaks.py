# LeetCode 3892. Minimum Operations to Achieve At Least K Peaks — Hard
# https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/
# Submission 2203355727 — Accepted, Python3
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # My thinking: raising a peak never hurts another peak,
        # because peaks are never adjacent and a peak's raised
        # value is not a neighbour of any other peak, and
        # raising a non-peak only makes peaks harder. So each
        # index i has an independent price: how much it must
        # rise to beat both of its original neighbours, or 0
        # if it already does. The task becomes picking k
        # non-adjacent indices of minimum total price on a
        # cycle. That is a small DP over a path — dp0[t] the
        # cheapest price with t peaks and the last index not
        # taken, dp1[t] with it taken — run twice to break the
        # cycle: once with index 0 forbidden, once with index
        # 0 taken (paying its price and forbidding its two
        # neighbours). More than n // 2 peaks is impossible on
        # a cycle, and k = 0 costs nothing.
        n = len(nums)
        if k == 0:
            return 0
        if k > n // 2:
            return -1
        INF = float('inf')
        costs = [max(0, max(nums[i - 1], nums[(i + 1) % n]) + 1 - nums[i])
                 for i in range(n)]

        def path_dp(cs, t):
            dp0 = [0] + [INF] * t
            dp1 = [INF] * (t + 1)
            for c in cs:
                ndp0 = [a if a < b else b for a, b in zip(dp0, dp1)]
                ndp1 = [INF] + [dp0[j] + c for j in range(t)]
                dp0, dp1 = ndp0, ndp1
            return min(dp0[t], dp1[t])

        best = path_dp(costs[1:], k)
        if k >= 1:
            best = min(best, costs[0] + path_dp(costs[2:n - 1], k - 1))
        return best if best < INF else -1
