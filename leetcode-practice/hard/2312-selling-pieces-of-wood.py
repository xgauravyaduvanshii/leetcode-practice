# LeetCode 2312. Selling Pieces of Wood — Hard
# https://leetcode.com/problems/selling-pieces-of-wood/
# Submission 2201672968 — Accepted, Python3
#
# My thinking: any board is either sold as
# it stands or split once — so I fill a
# table of best prices for every size and
# let each size take the best of selling
# whole or cutting across or down.

class Solution:
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        price = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            price[h][w] = p
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h in range(1, m + 1):
            for w in range(1, n + 1):
                best = price[h][w]
                for k in range(1, w // 2 + 1):
                    best = max(best, dp[h][k] + dp[h][w - k])
                for k in range(1, h // 2 + 1):
                    best = max(best, dp[k][w] + dp[h - k][w])
                dp[h][w] = best
        return dp[m][n]
