# LeetCode 375. Guess Number Higher or Lower II — Medium
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# Submission 2198763406 — Accepted, Python3
#
# My thinking: for any range I try every guess and
# pay the worst of the two sides it splits into.
# The cheapest worst case over all guesses is the
# answer, built up from short ranges to long ones.

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                dp[start][end] = min(
                    guess + max(dp[start][guess - 1], dp[guess + 1][end])
                    for guess in range(start, end + 1)
                )
        return dp[1][n]
