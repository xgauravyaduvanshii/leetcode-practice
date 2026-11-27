# LeetCode 120. Triangle — Medium
# https://leetcode.com/problems/triangle/
# Submission 2204014193 — Accepted, Python3
#
# My thinking: I work from the bottom row up. For each number I add the
# cheaper of the two numbers directly below it, because from any spot
# the only moves are down-left and down-right. Reusing one list of the
# running totals keeps the memory down to one row, and once I reach the
# top, the first entry is the cheapest path from the top to the bottom.

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
        return dp[0]
