# LeetCode 2412. Minimum Money Required Before Transactions — Hard
# https://leetcode.com/problems/minimum-money-required-before-transactions/
# Submission 2201725587 — Accepted, Python3
#
# My thinking: the worst order runs every
# losing deal first — a deal done after
# them all must be paid for out of what is
# left, so I add every loss to the dearest
# gaining deal's cost and to the biggest
# cashback a losing deal ever returns, and
# take the larger of the two.

class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        total_loss = 0
        max_cost_gain = 0
        max_cashback_loss = 0
        for cost, cashback in transactions:
            if cost > cashback:
                total_loss += cost - cashback
                max_cashback_loss = max(max_cashback_loss, cashback)
            else:
                max_cost_gain = max(max_cost_gain, cost)
        return max(total_loss + max_cost_gain, total_loss + max_cashback_loss)
