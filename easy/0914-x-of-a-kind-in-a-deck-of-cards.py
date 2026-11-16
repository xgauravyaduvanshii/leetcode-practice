# LeetCode 914. X of a Kind in a Deck of Cards — Easy
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Submission 2197541754 — Accepted, Python3
#
# My thinking: I count how many of each card there
# are. For the deck to split into equal groups of
# size X, every count has to be a multiple of X —
# which means X has to divide the greatest common
# divisor of all the counts. So I take the GCD of
# the counts and check it is at least 2.

from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        counts = {}
        for card in deck:
            counts[card] = counts.get(card, 0) + 1
        g = 0
        for count in counts.values():
            g = gcd(g, count)
        return g >= 2
