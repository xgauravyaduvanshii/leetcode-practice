# LeetCode 3077. Maximum Strength of K Disjoint Subarrays — Hard
# https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/
# Submission 2201924873 — Accepted, Python3
#
# My thinking: the j-th subarray is
# weighted by (k - j + 1), with the sign
# flipping each time, so I build the
# answer one subarray at a time. For
# each count j I sweep the array once,
# keeping the best place the j-th
# subarray could have started — its
# earlier strength minus the weighted
# prefix before it — and either extend
# the best subarray so far or end a new
# one here. Prefix sums make every
# subarray sum a subtraction.

from typing import List

INF = 10**30


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        # dp_prev[i]: best strength with j-1 subarrays in nums[:i+1].
        dp_prev = [0] * n
        for j in range(1, k + 1):
            coef = (k - j + 1) * (1 if j % 2 == 1 else -1)
            dp_cur = [-INF] * n
            best = -INF  # best of dp_prev[s-1] - coef * prefix[s]
            for i in range(n):
                prev = dp_prev[i - 1] if i > 0 else (0 if j == 1 else -INF)
                cand = prev - coef * prefix[i]
                if cand > best:
                    best = cand
                val = coef * prefix[i + 1] + best
                dp_cur[i] = val if i == 0 else max(dp_cur[i - 1], val)
            dp_prev = dp_cur
        return dp_prev[n - 1]
