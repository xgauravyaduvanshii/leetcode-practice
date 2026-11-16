# LeetCode 1518. Water Bottles — Easy
# https://leetcode.com/problems/water-bottles/
# Submission 2197583463 — Accepted, Python3
#
# My thinking: I drink the bottles I have and trade
# the empty ones for new full ones, as long as I
# have enough empties. Each trade gives me new
# bottles to drink and new empties left over, and
# I keep going until I cannot trade any more.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            exchanged = empty // numExchange
            total += exchanged
            empty = exchanged + empty % numExchange
        return total
