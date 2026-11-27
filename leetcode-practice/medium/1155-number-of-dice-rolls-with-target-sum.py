# LeetCode 1155. Number of Dice Rolls With Target Sum — Medium
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Submission 2199008074 — Accepted, Python3
#
# My thinking: I count the ways after each die
# with a running window — the ways to reach a
# total are the ways to reach the last k totals
# before it, one die face back.

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            new = [0] * (target + 1)
            running = 0
            for total in range(1, target + 1):
                running = (running + dp[total - 1]) % mod
                if total - k - 1 >= 0:
                    running = (running - dp[total - k - 1]) % mod
                new[total] = running
            dp = new
        return dp[target]
