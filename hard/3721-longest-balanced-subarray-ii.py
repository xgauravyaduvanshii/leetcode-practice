# LeetCode 3721. Longest Balanced Subarray II — Hard
# https://leetcode.com/problems/longest-balanced-subarray-ii/
# Submission 2203064202 — Accepted, Python3
import numpy as np
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # My thinking: give every distinct value a sign, +1
        # for odd and -1 for even, so a subarray is balanced
        # exactly when the signs of its distinct values sum to
        # zero. Fix the right end r and keep, for every possible
        # left end l, the balance of nums[l..r]. When r moves
        # one step right to a value seen before at p, only the
        # starts l in (p, r] gain a newly distinct value — the
        # starts at or before p already contain it — so that
        # step is one range add of the sign over [p+1, r]. The
        # longest balanced subarray ending at r then starts at
        # the smallest l whose balance is zero, and the answer
        # is the best of those over all r. The range adds and
        # the leftmost-zero search run on a sqrt decomposition
        # of the balance array, with a lazy add per block, so
        # each step is a handful of vectorised numpy ops.
        n = len(nums)
        if n == 0:
            return 0
        size = 512
        nb = (n + size - 1) // size
        val = np.zeros(n, dtype=np.int64)
        lazy = np.zeros(nb, dtype=np.int64)
        mn = np.zeros(nb, dtype=np.int64)
        mx = np.zeros(nb, dtype=np.int64)
        last = {}
        ans = 0
        for r, x in enumerate(nums):
            s = 1 if x & 1 else -1
            p = last.get(x, -1)
            last[x] = r
            lo = p + 1
            bl = lo // size
            br = r // size
            if bl == br:
                val[lo:r + 1] += s
                seg = val[bl * size:(bl + 1) * size]
                mn[bl] = seg.min()
                mx[bl] = seg.max()
            else:
                end = (bl + 1) * size
                val[lo:end] += s
                seg = val[bl * size:end]
                mn[bl] = seg.min()
                mx[bl] = seg.max()
                start = br * size
                val[start:r + 1] += s
                seg = val[start:(br + 1) * size]
                mn[br] = seg.min()
                mx[br] = seg.max()
                if br - bl > 1:
                    lazy[bl + 1:br] += s
            # Leftmost l in [0, r] whose balance is zero: the
            # first block whose [min, max] range covers zero,
            # then the first zero inside that block. (The tail
            # of the last block past r still reads zero, so a
            # zero found there past r means no balanced
            # subarray ends at r.)
            emin = mn[:br + 1] + lazy[:br + 1]
            emax = mx[:br + 1] + lazy[:br + 1]
            cond = (emin <= 0) & (emax >= 0)
            b = int(np.argmax(cond))
            if cond[b]:
                seg = val[b * size:(b + 1) * size] + int(lazy[b])
                zeros = np.flatnonzero(seg == 0)
                if len(zeros):
                    l = int(zeros[0]) + b * size
                    if l <= r:
                        ans = max(ans, r - l + 1)
        # The judge wants a plain int, not a numpy scalar.
        return int(ans)
