# LeetCode 1475. Final Prices With a Special Discount in a Shop — Easy
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Submission 2197581624 — Accepted, Python3
#
# My thinking: for each price, the discount is the
# first later price that is no bigger than it. I
# scan to the right until I find one and subtract
# it. If there is none, the price stays as it is.

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result = prices[:]
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result[i] -= prices[j]
                    break
        return result
