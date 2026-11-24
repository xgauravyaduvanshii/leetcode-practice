# LeetCode 3336. Find the Number of Subsequences With Equal GCD — Hard
# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/
# Submission 2202384198 — Accepted, Python3
from math import gcd
from typing import List

MOD = 10 ** 9 + 7
MAXV = 200


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        # My thinking: I build the two disjoint subsequences element by
        # element, tracking the pair of their GCDs so far (0 means that side
        # is still empty). Each new number either is skipped, joins the
        # first subsequence (gcd(g1, a)), or joins the second (gcd(g2, a)).
        # The DP is a 201x201 grid over GCD pairs, but I only iterate rows
        # that hold a non-zero count, and a precomputed GCD table answers
        # every gcd(g, a) lookup. At the end I add up the counts of all
        # pairs (g, g) with g > 0, which are exactly the pairs of non-empty
        # subsequences with equal GCD.
        dp = [[0] * (MAXV + 1) for _ in range(MAXV + 1)]
        dp[0][0] = 1
        table = [[gcd(g, a) for a in range(MAXV + 1)] for g in range(MAXV + 1)]
        active = {0}
        for a in nums:
            ndp = [row[:] for row in dp]
            new_active = set(active)
            for g1 in list(active):
                ng1 = table[g1][a]
                src = dp[g1]
                dst = ndp[ng1]
                for g2 in range(MAXV + 1):
                    v = src[g2]
                    if v:
                        dst[g2] = (dst[g2] + v) % MOD
                        ng2 = table[g2][a]
                        ndp[g1][ng2] = (ndp[g1][ng2] + v) % MOD
                        new_active.add(ng1)
            dp = ndp
            active = new_active
        ans = 0
        for g in range(1, MAXV + 1):
            ans = (ans + dp[g][g]) % MOD
        return ans
