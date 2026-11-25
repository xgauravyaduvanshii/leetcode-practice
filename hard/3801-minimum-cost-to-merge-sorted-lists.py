# LeetCode 3801. Minimum Cost to Merge Sorted Lists — Hard
# https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/
# Submission 2203185205 — Accepted, Python3
import numpy as np
from typing import List


class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        # My thinking: merging two lists costs their total
        # length plus the gap between their medians, and the
        # merged list depends only on which original lists went
        # into it, not on the merge order — so the whole problem
        # is a DP over subsets. For every nonempty subset I
        # precompute its size and its left median (the
        # ((size + 1) // 2)-th smallest value, found by binary
        # searching the sorted distinct values with per-list
        # upper-bound counts, all vectorised with numpy). Then
        # f[mask] is the cheapest cost to merge that subset into
        # one list: split it into two nonempty parts, pay their
        # costs plus the median gap, plus the size of the subset
        # itself for the final merge's length part. The answer
        # is f[full mask].
        n = len(lists)
        vals = np.array(sorted({x for lst in lists for x in lst}), dtype=np.int64)
        nvals = len(vals)
        # le[i][j] = how many elements of lists[i] are <= vals[j].
        le = np.zeros((n, nvals), dtype=np.int32)
        for i, lst in enumerate(lists):
            le[i] = np.searchsorted(lst, vals, side="right")
        full = 1 << n
        # cnt_le[mask][j] = elements of the subset <= vals[j].
        cnt_le = np.zeros((full, nvals), dtype=np.int32)
        for mask in range(1, full):
            lsb = mask & -mask
            i = lsb.bit_length() - 1
            cnt_le[mask] = cnt_le[mask ^ lsb] + le[i]
        cnt = cnt_le[:, -1].astype(np.int64)
        need = (cnt + 1) // 2
        med = np.zeros(full, dtype=np.int64)
        for mask in range(1, full):
            j = int(np.searchsorted(cnt_le[mask], need[mask], side="left"))
            med[mask] = vals[j]
        med = med.tolist()
        cnt = cnt.tolist()
        INF = float("inf")
        f = [INF] * full
        for i in range(n):
            f[1 << i] = 0
        for mask in range(1, full):
            if mask & (mask - 1) == 0:
                continue
            best = INF
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if sub <= other:
                    cand = f[sub] + f[other] + abs(med[sub] - med[other])
                    if cand < best:
                        best = cand
                sub = (sub - 1) & mask
            f[mask] = best + cnt[mask]
        return f[full - 1]
