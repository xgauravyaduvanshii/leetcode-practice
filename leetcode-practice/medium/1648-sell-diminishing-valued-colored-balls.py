# LeetCode 1648. Sell Diminishing-Valued Colored Balls — Medium
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
# Submission 2199901009 — Accepted, Python3
#
# My thinking: I sell level by level from the
# top, whole levels at a time. A level's value
# is an arithmetic sum, and the last partial
# level sells what is left at its price.

from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mod = 10 ** 9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)
        profit = 0
        width = 1
        for i in range(len(inventory) - 1):
            gap = inventory[i] - inventory[i + 1]
            balls = gap * width
            if orders >= balls:
                profit += width * (inventory[i] + inventory[i + 1] + 1) * gap // 2
                orders -= balls
            else:
                full_rounds = orders // width
                profit += width * (inventory[i] + inventory[i] - full_rounds + 1) * full_rounds // 2
                leftover = orders % width
                profit += leftover * (inventory[i] - full_rounds)
                orders = 0
                break
            width += 1
        return profit % mod
