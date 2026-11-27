# LeetCode 1737. Change Minimum Characters to Satisfy One of Three Conditions — Medium
# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/
# Submission 2199922922 — Accepted, Python3
#
# My thinking: I try every split letter. For
# the two ordering conditions I count how many
# letters sit on the wrong side of the split;
# for the third I count how many letters are
# not the chosen one. The cheapest wins.

from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ca = Counter(a)
        cb = Counter(b)
        best = len(a) + len(b)
        for letter in range(26):
            cost = len(a) - ca.get(chr(97 + letter), 0) + len(b) - cb.get(chr(97 + letter), 0)
            best = min(best, cost)
        for split in range(1, 26):
            cost1 = sum(ca.get(chr(97 + c), 0) for c in range(split, 26)) + sum(cb.get(chr(97 + c), 0) for c in range(split))
            cost2 = sum(cb.get(chr(97 + c), 0) for c in range(split, 26)) + sum(ca.get(chr(97 + c), 0) for c in range(split))
            best = min(best, cost1, cost2)
        return best
