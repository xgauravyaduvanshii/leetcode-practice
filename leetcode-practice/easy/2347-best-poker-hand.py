# LeetCode 2347. Best Poker Hand — Easy
# https://leetcode.com/problems/best-poker-hand/
# Submission 2197623968 — Accepted, Python3
#
# My thinking: if all five suits match it's a flush.
# Otherwise the best hand depends on the most
# repeated rank — three or more is Three of a Kind,
# two is a Pair, and anything else is a High Card.

from collections import Counter


class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        counts = Counter(ranks)
        if max(counts.values()) >= 3:
            return "Three of a Kind"
        if max(counts.values()) == 2:
            return "Pair"
        return "High Card"
