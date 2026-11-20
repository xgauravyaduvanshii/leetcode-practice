# LeetCode 1599. Maximum Profit of Operating a Centennial Wheel — Medium
# https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/
# Submission 2199887307 — Accepted, Python3
#
# My thinking: I simulate every rotation,
# boarding at most four waiting customers
# each time. I remember the rotation where
# the running profit peaked — and return -1
# when it never rose above zero.

from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        profit = 0
        best_profit = 0
        best_round = -1
        rounds = 0
        i = 0
        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
                i += 1
            board = min(4, waiting)
            waiting -= board
            profit += board * boardingCost - runningCost
            rounds += 1
            if profit > best_profit:
                best_profit = profit
                best_round = rounds
        return best_round
