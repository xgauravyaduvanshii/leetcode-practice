# LeetCode 3193. Count the Number of Inversions — Hard
# https://leetcode.com/problems/count-the-number-of-inversions/
# Submission 2202072204 — Accepted, Python3
#
# My thinking: I build permutations one
# element at a time: inserting the new
# largest element into a permutation of
# length L adds anywhere from 0 to L-1
# inversions, so the counts follow a
# sliding-window DP over inversion
# totals, kept in prefix sums. Whenever
# a requirement pins the count at some
# length, I zero out every other count
# and continue.

from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        MAXC = 400
        req = {e: c for e, c in requirements}
        dp = [0] * (MAXC + 1)
        dp[0] = 1
        for length in range(1, n + 1):
            pref = [0] * (MAXC + 1)
            s = 0
            for j in range(MAXC + 1):
                s = (s + dp[j]) % MOD
                pref[j] = s
            ndp = [0] * (MAXC + 1)
            for j in range(MAXC + 1):
                val = pref[j]
                if j - length >= 0:
                    val -= pref[j - length]
                ndp[j] = val % MOD
            if length - 1 in req:
                cnt = req[length - 1]
                keep = ndp[cnt] if cnt <= MAXC else 0
                ndp = [0] * (MAXC + 1)
                if cnt <= MAXC:
                    ndp[cnt] = keep
            dp = ndp
        return dp[req[n - 1]] % MOD
