# LeetCode 3757. Number of Effective Subsequences — Hard
# https://leetcode.com/problems/number-of-effective-subsequences/
# Submission 2203159821 — Accepted, Python3
import numpy as np
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def countEffective(self, nums: List[int]) -> int:
        # My thinking: a subsequence is effective exactly when
        # removing it kills at least one bit of the total OR.
        # For each bit b of the total OR, let E_b be the event
        # that the subsequence contains every element carrying
        # b — then the subsequence is effective exactly when at
        # least one E_b happens. By inclusion-exclusion over
        # the bits, the count of subsequences where a chosen
        # set U of events all happen is 2 raised to the number
        # of elements carrying none of U's bits. Compressing
        # each number to its mask over the total OR's bits
        # (at most 20), a fully vectorised SOS DP over the
        # 2^k masks counts, for every mask, how many elements
        # sit inside it, and the signed sum over all masks
        # gives the number of non-effective subsequences; the
        # answer is 2^n minus that, modulo 1e9 + 7.
        total_or = 0
        for x in nums:
            total_or |= x
        bits = [b for b in range(20) if (total_or >> b) & 1]
        k = len(bits)
        n = len(nums)
        arr = np.array(nums, dtype=np.int64)
        masks = np.zeros(n, dtype=np.int64)
        for j, b in enumerate(bits):
            masks |= ((arr >> b) & 1) << j
        m = 1 << k
        h = np.bincount(masks, minlength=m).astype(np.int64)
        for j in range(k):
            step = 1 << j
            h = h.reshape(-1, 2 * step)
            h[:, step:] += h[:, :step]
            h = h.reshape(-1)
        pow2 = np.empty(n + 1, dtype=np.int64)
        pow2[0] = 1
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        vals = pow2[h]
        idx = np.arange(m)
        parity = np.zeros(m, dtype=np.int64)
        for j in range(k):
            parity += (idx >> j) & 1
        # (-1)^(k - popcount): +1 when k and popcount agree.
        sign = np.where((parity & 1) == (k & 1), 1, -1)
        # The signed sum stays within about 1e15, safe in int64.
        total = int(np.sum(sign * vals))
        return (int(pow2[n]) - total) % MOD
