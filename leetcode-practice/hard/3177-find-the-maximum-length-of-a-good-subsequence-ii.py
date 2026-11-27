# LeetCode 3177. Find the Maximum Length of a Good Subsequence II — Hard
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/
# Submission 2202060224 — Accepted, Python3
#
# My thinking: for each allowed number
# of changes t I keep, per value, the
# longest good subsequence ending in
# that value, plus the best and
# second-best lengths over all values.
# Extending by x either repeats x,
# spends a change on a different best
# value, or continues the same value
# from t-1 — and I update the two bests
# so the next value can pick a different
# one.

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        K = k
        f = [dict() for _ in range(K + 1)]
        best1_val = [None] * (K + 1)
        best1_len = [0] * (K + 1)
        best2_len = [0] * (K + 1)
        for x in nums:
            for t in range(K, -1, -1):
                old = f[t].get(x, 0)
                cand = old + 1
                if t > 0:
                    prev_same = f[t - 1].get(x, 0)
                    if prev_same + 1 > cand:
                        cand = prev_same + 1
                    b = best1_len[t - 1] if best1_val[t - 1] != x else best2_len[t - 1]
                    if b + 1 > cand:
                        cand = b + 1
                if cand > old:
                    f[t][x] = cand
                    if best1_val[t] == x:
                        best1_len[t] = cand
                    elif cand > best1_len[t]:
                        best2_len[t] = best1_len[t]
                        best1_len[t] = cand
                        best1_val[t] = x
                    elif cand > best2_len[t]:
                        best2_len[t] = cand
        return best1_len[K]
