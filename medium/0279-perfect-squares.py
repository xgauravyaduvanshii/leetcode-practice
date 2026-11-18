# LeetCode 279. Perfect Squares — Medium
# https://leetcode.com/problems/perfect-squares/
# Submission 2198728184 — Accepted, Python3
#
# My thinking: the fewest squares for a number is one
# more than the fewest squares for what remains after
# taking away one square. I build that up from 1 to n,
# trying every square that fits at each step.

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [0] + [float("inf")] * n
        for target in range(1, n + 1):
            for square in squares:
                if square > target:
                    break
                dp[target] = min(dp[target], dp[target - square] + 1)
        return dp[n]
