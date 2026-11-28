# LeetCode 2466. Count Ways To Build Good Strings — Medium
# https://leetcode.com/problems/count-ways-to-build-good-strings/
# Submission 2204960817 — Accepted, Python3
#
# My thinking: dp[i] counts the strings of length exactly i. A
# string of length i ends in a block of `zero` zeros or a block of
# `one` ones, so dp[i] = dp[i - zero] + dp[i - one]. The answer is
# the sum of dp[low] through dp[high], all modulo 1e9 + 7.
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        return sum(dp[low:high + 1]) % MOD
