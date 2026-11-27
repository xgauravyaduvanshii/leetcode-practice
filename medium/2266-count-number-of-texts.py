# LeetCode 2266. Count Number of Texts — Medium
# https://leetcode.com/problems/count-number-of-texts/
# Submission 2204521401 — Accepted, Python3
#
# My thinking: the pressed keys split into runs of equal digits, and
# each run is decoded independently. A run of length L on a key with 3
# letters can be split into groups of 1, 2 or 3 presses, and a key with
# 4 letters (7 or 9) also allows groups of 4. I count the groupings with
# a small DP over the run and multiply the counts across runs, all
# modulo 10^9 + 7.
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] = (dp[i] + dp[i - 2]) % MOD
            if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3]:
                dp[i] = (dp[i] + dp[i - 3]) % MOD
            if i >= 4 and pressedKeys[i - 1] in '79' and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3] == pressedKeys[i - 4]:
                dp[i] = (dp[i] + dp[i - 4]) % MOD
        return dp[n] % MOD
