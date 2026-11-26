# LeetCode 4041. Minimum Operations to Form Subset Sum II — Hard
# https://leetcode.com/problems/minimum-operations-to-form-subset-sum-ii/
# Submission 2203529023 — Accepted, Python3
from typing import List

import numpy as np


class Solution:
    def minOperations(self, nums: List[int], sum: int) -> int:
        # My thinking: each element can be divided and
        # doubled in any order, and any sequence of d
        # divisions and m doublings lands on (x >> d) << m
        # — dividing drops low bits, doubling appends
        # zeroes — so for every d the reachable values are
        # base, 2*base, 4*base, ... with costs d, d+1,
        # d+2, ... . Keep the cheapest cost for each value
        # up to sum: values above sum can never join a
        # subset summing to sum, and doubling past sum and
        # dividing back only wastes operations, since
        # floor(2u / 2) is exactly u again. Then it is a
        # 0/1 knapsack over the target sum: dp[s] is the
        # fewest operations to reach sum s with the elements
        # handled so far, and each element either stays out
        # or joins with one of its reachable values. The
        # numpy min-plus update applies one value at a time
        # against the previous layer, so no element is ever
        # used twice.
        INF = 10 ** 9
        dp = np.full(sum + 1, INF, dtype=np.int64)
        dp[0] = 0
        for x in nums:
            opts = {}
            d = 0
            while True:
                base = x >> d
                v, c = base, d
                while v <= sum:
                    if v not in opts or c < opts[v]:
                        opts[v] = c
                    if v == 0:
                        break
                    v *= 2
                    c += 1
                if base == 0:
                    break
                d += 1
            ndp = dp.copy()
            for v, c in opts.items():
                if v == 0:
                    continue
                cand = dp[:sum + 1 - v] + c
                np.minimum(ndp[v:], cand, out=ndp[v:])
            dp = ndp
        return int(dp[sum]) if dp[sum] < INF else -1
