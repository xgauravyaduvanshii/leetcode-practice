# LeetCode 1128. Number of Equivalent Domino Pairs — Easy
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# Submission 2197558867 — Accepted, Python3
#
# My thinking: a domino is the same flipped over, so
# I normalise each one by putting the smaller
# number first. Then I count how many of each type
# I have seen — every earlier domino of the same
# type pairs with this one.

from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        counts = Counter()
        pairs = 0
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            pairs += counts[key]
            counts[key] += 1
        return pairs
