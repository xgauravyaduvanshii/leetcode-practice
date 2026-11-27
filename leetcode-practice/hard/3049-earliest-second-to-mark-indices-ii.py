# LeetCode 3049. Earliest Second to Mark Indices II — Hard
# https://leetcode.com/problems/earliest-second-to-mark-indices-ii/
# Submission 2201916904 — Accepted, Python3
#
# My thinking: I binary-search the
# earliest second and test a candidate
# directly. An index is reset at its
# first change second — the earliest
# reset leaves the most room to mark it
# afterwards. Resetting an index saves
# its decrements but costs the reset
# second itself, so I keep the resets
# with the biggest savings, dropping the
# smallest whenever too many resets
# crowd one stretch: resets whose first
# change falls in [t, x) each need two
# seconds there (the reset and its mark),
# so at most (x - t) // 2 of them fit.
# Whatever is left must fit in the x
# seconds: one mark per index, the
# remaining decrements, and the resets.

from typing import List
import heapq


class Solution:
    def earliestSecondToMarkIndices(
        self, nums: List[int], changeIndices: List[int]
    ) -> int:
        n = len(nums)
        m = len(changeIndices)

        def can(x: int) -> bool:
            # First change second (0-based) of each index, or -1.
            first = [-1] * n
            for s in range(x):
                i = changeIndices[s] - 1
                if first[i] < 0:
                    first[i] = s
            total_dec = sum(nums)
            # (first second, saving) for each reset worth doing.
            cands = [
                (first[i], nums[i] - 1)
                for i in range(n)
                if nums[i] >= 2 and first[i] >= 0
            ]
            cands.sort(reverse=True)  # latest first change first
            heap = []  # min-heap of savings kept so far
            saving = 0
            for f, sv in cands:
                heapq.heappush(heap, sv)
                saving += sv
                cap = (x - f) // 2
                while len(heap) > cap:
                    saving -= heapq.heappop(heap)
            # Marks + leftover decrements + resets must fit in x.
            return n + total_dec - saving <= x

        if not can(m):
            return -1
        lo, hi = 1, m
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
