# LeetCode 3806. Maximum Bitwise AND After Increment Operations — Hard
# https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/
# Submission 2203188334 — Accepted, Python3
import numpy as np
from typing import List


class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        # My thinking: build the answer bit by bit from the top
        # down — a bit can stay set only if m numbers can be
        # raised to values containing all the bits chosen so
        # far, within k increments in total. Raising x to cover
        # a target is cheapest by fixing the lowest missing bit
        # and everything below it: if j is the highest bit where
        # the target has a 1 that x lacks, the cheapest y >= x
        # with all target bits is x rounded up to the target's
        # low j bits, costing (target & mask) - (x & mask) with
        # mask = 2^j - 1 (and 0 when x already covers the
        # target). The m cheapest such costs decide whether the
        # bit survives; all of this is vectorised with numpy
        # (bit lengths from log2, cheapest m via partition), so
        # each bit costs one pass over the array.
        a = np.array(nums, dtype=np.int64)
        mx = (int(a.max()) + k).bit_length()
        ans = 0
        for bit in range(mx - 1, -1, -1):
            target = ans | (1 << bit)
            missing = target & ~a
            j = np.zeros(a.shape, dtype=np.int64)
            nz = missing > 0
            j[nz] = np.floor(np.log2(missing[nz])).astype(np.int64) + 1
            mask = (np.int64(1) << j) - 1
            cost = (target & mask) - (a & mask)
            cheapest = np.partition(cost, m - 1)[:m].sum()
            if cheapest <= k:
                ans = target
        return ans
