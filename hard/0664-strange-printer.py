# LeetCode 664. Strange Printer — Hard
# https://leetcode.com/problems/strange-printer/
# Submission 2198665768 — Accepted, Python3
#
# My thinking: for a stretch of the string I try
# printing the last character on its own, and then I
# try merging it with every matching character inside
# the stretch — printing the two together costs one
# turn instead of two, and the middle part is solved
# separately.

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                dp[left][right] = dp[left][right - 1] + 1
                for middle in range(left, right):
                    if s[middle] == s[right]:
                        merged = dp[left][middle] + (
                            dp[middle + 1][right - 1] if middle + 1 <= right - 1 else 0
                        )
                        dp[left][right] = min(dp[left][right], merged)
        return dp[0][n - 1]
