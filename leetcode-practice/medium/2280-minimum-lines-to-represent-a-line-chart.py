# LeetCode 2280. Minimum Lines to Represent a Line Chart — Medium
# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/
# Submission 2204633148 — Accepted, Python3
#
# My thinking: sort the points by day. Two neighbouring segments lie on
# the same line exactly when their slopes are equal, and I compare slopes
# by cross-multiplication ((y2-y1)*(x3-x2) vs (y3-y2)*(x2-x1)) so no
# division or floating point is needed. Every time the slope changes I
# start a new line; with at most one point the answer is zero.
class Solution:
    def minimumLines(self, stockPrices: list[list[int]]) -> int:
        stockPrices.sort()
        n = len(stockPrices)
        if n <= 1:
            return 0
        ans = 1
        for i in range(2, n):
            x1, y1 = stockPrices[i - 2]
            x2, y2 = stockPrices[i - 1]
            x3, y3 = stockPrices[i]
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                ans += 1
        return ans
