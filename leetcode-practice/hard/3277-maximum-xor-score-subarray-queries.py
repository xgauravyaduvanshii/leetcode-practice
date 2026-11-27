# LeetCode 3277. Maximum XOR Score Subarray Queries — Hard
# https://leetcode.com/problems/maximum-xor-score-subarray-queries/
# Submission 2202174987 — Accepted, Python3
#
# My thinking: the XOR of a subarray is the XOR
# of two adjacent subarrays of the level below,
# so I build the XOR triangle row by row, and
# alongside it the best XOR seen for every
# (start, length). A query [l, r] is then just
# best[length r-l][l]. I use numpy when it is
# available and a plain list fallback otherwise.

from typing import List


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        try:
            import numpy as np
            cur = np.array(nums, dtype=np.int64)
            best = cur.copy()
            best_by_len = [best]
            for _ in range(2, n + 1):
                prev_best = best
                cur = cur[:-1] ^ cur[1:]
                best = np.maximum(np.maximum(cur, prev_best[:-1]), prev_best[1:])
                best_by_len.append(best)
            return [int(best_by_len[r - l][l]) for l, r in queries]
        except Exception:
            cur = list(nums)
            best = cur[:]
            best_by_len = [best]
            for _ in range(2, n + 1):
                prev_best = best
                cur = [a ^ b for a, b in zip(cur, cur[1:])]
                best = [max(x, y, z) for x, y, z in zip(cur, prev_best, prev_best[1:])]
                best_by_len.append(best)
            return [best_by_len[r - l][l] for l, r in queries]
