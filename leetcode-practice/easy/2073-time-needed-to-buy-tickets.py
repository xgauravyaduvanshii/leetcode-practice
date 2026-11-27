# LeetCode 2073. Time Needed to Buy Tickets — Easy
# https://leetcode.com/problems/time-needed-to-buy-tickets/
# Submission 2197611766 — Accepted, Python3
#
# My thinking: I don't need to simulate the queue —
# I just add up how many tickets each person buys
# before person k finishes. People before k buy up
# to k's full amount, and people after k buy at most
# one less than that.

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        total = 0
        for i, t in enumerate(tickets):
            if i <= k:
                total += min(t, tickets[k])
            else:
                total += min(t, tickets[k] - 1)
        return total
