# LeetCode 3317. Find the Number of Possible Ways for an Event — Hard
# https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/
# Submission 2202323581 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        # My thinking: fix the number k of non-empty stages. The performers
        # split into k non-empty unlabelled groups in S(n, k) ways (Stirling
        # numbers of the second kind), the k stages are chosen and ordered in
        # P(x, k) = x * (x-1) * ... * (x-k+1) ways, and each of the k bands
        # gets one of y scores, giving y^k. I sum that product over all k.
        k_max = min(n, x)
        stir = [0] * (k_max + 1)
        stir[0] = 1
        for i in range(1, n + 1):
            nxt = [0] * (k_max + 1)
            for k in range(1, min(i, k_max) + 1):
                nxt[k] = (k * stir[k] + stir[k - 1]) % MOD
            stir = nxt
        ans = 0
        perm = 1
        pow_y = 1
        for k in range(1, k_max + 1):
            perm = perm * (x - k + 1) % MOD
            pow_y = pow_y * y % MOD
            ans = (ans + perm * stir[k] % MOD * pow_y) % MOD
        return ans
