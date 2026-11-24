# LeetCode 3480. Maximize Subarrays After Removing One Conflicting Pair — Hard
# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/
# Submission 2202668120 — Accepted 642/642, Python3
#
# My thinking: a subarray ending at r is bad exactly when its left end is
# at or before the biggest left end a of a remaining pair whose right end
# is at or before r, so with M(r) for that biggest left end the number of
# bad subarrays is the sum of M(r). Removing a pair can only help when it
# is the unique biggest left end for its right end and that right end is a
# new record for M; the gain is how far M drops over the stretch until the
# next record, never below the previous record or the second-biggest left
# end for that right end. I take the best such gain over all record pairs,
# or zero when no removal helps.

from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        by_hi = defaultdict(list)
        for a, b in conflictingPairs:
            lo, hi = (a, b) if a < b else (b, a)
            by_hi[hi].append(lo)
        A = {}
        for hi, los in by_hi.items():
            los.sort(reverse=True)
            mx = los[0]
            cnt = 0
            for x in los:
                if x == mx:
                    cnt += 1
                else:
                    break
            second = los[cnt] if cnt < len(los) else 0
            A[hi] = (mx, cnt, second)
        his = sorted(A)
        total_bad = 0
        cur_max = 0
        hi_idx = 0
        for r in range(1, n + 1):
            while hi_idx < len(his) and his[hi_idx] == r:
                cur_max = max(cur_max, A[his[hi_idx]][0])
                hi_idx += 1
            total_bad += cur_max
        records = []
        cur = 0
        for hi in his:
            if A[hi][0] > cur:
                records.append(hi)
                cur = A[hi][0]
        max_gain = 0
        for idx, hi in enumerate(records):
            X, cnt, second = A[hi]
            if cnt >= 2:
                continue
            prev_rec = A[records[idx - 1]][0] if idx > 0 else 0
            nxt = records[idx + 1] if idx + 1 < len(records) else n + 1
            P = prev_rec
            cur_r = hi
            gain = 0
            inter = [h for h in his if hi < h < nxt]
            for h in inter:
                if P < X:
                    gain += (X - max(P, second)) * (h - cur_r)
                P = max(P, A[h][0])
                cur_r = h
            if P < X:
                gain += (X - max(P, second)) * (nxt - cur_r)
            max_gain = max(max_gain, gain)
        total = n * (n + 1) // 2
        return total - total_bad + max_gain
