# LeetCode 1039. Minimum Score Triangulation of Polygon — Medium
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
# Submission 2198991640 — Accepted, Python3
#
# My thinking: I try every split of the polygon
# into two smaller polygons plus one triangle.
# The cheapest way to triangulate each side is
# already known, so the answer builds up from
# the smallest pieces.

from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = min(
                    dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    for k in range(i + 1, j)
                )
        return dp[0][n - 1]
