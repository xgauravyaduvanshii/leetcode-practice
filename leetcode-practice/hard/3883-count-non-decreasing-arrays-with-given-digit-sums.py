# LeetCode 3883. Count Non Decreasing Arrays With Given Digit Sums — Hard
# https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/
# Submission 2203339812 — Accepted, Python3
from itertools import accumulate
from typing import List


class Solution:
    def countArrays(self, digitSum: List[int]) -> int:
        # My thinking: the value at each position is a number
        # from 0 to 5000 whose digit sum is fixed, so first
        # list, for every digit sum, the numbers that have it.
        # Then dp over the value axis: dp[v] is the number of
        # ways to fill the positions so far ending with value
        # v, which is the prefix sum of the previous dp over
        # all values up to v when v has the required digit
        # sum, and 0 otherwise. Prefix sums make each
        # position O(5000), and the answer is the sum of the
        # last dp, all modulo 1e9 + 7. A digit sum above 36
        # is impossible, since 4999 has the largest digit sum
        # in range, 36.
        MOD = 10 ** 9 + 7
        MAXV = 5000
        ds = [0] * (MAXV + 1)
        for v in range(1, MAXV + 1):
            ds[v] = ds[v // 10] + v % 10
        valid = [[] for _ in range(51)]
        for v in range(MAXV + 1):
            valid[ds[v]].append(v)
        prev = [0] * (MAXV + 1)
        for v in valid[digitSum[0]]:
            prev[v] = 1
        for i in range(1, len(digitSum)):
            s = digitSum[i]
            if s > 36:
                return 0
            pref = list(accumulate(prev))
            cur = [0] * (MAXV + 1)
            for v in valid[s]:
                cur[v] = pref[v] % MOD
            prev = cur
        return sum(prev) % MOD
