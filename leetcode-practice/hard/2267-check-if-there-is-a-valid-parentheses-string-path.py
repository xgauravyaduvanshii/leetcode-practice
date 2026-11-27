# LeetCode 2267. Check if There Is a Valid Parentheses String Path — Hard
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
# Submission 2201646221 — Accepted, Python3
#
# My thinking: a path is only alive while
# its balance never dips below zero, so I
# carry the set of balances each cell can
# still reach and ask whether zero survives
# to the far corner.

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        max_bal = (m + n) // 2
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                balances = set()
                if i > 0:
                    balances |= dp[i - 1][j]
                if j > 0:
                    balances |= dp[i][j - 1]
                if not balances:
                    continue
                for b in balances:
                    if grid[i][j] == '(':
                        nb = b + 1
                        if nb <= max_bal:
                            dp[i][j].add(nb)
                    else:
                        nb = b - 1
                        if nb >= 0:
                            dp[i][j].add(nb)
        return 0 in dp[m - 1][n - 1]
