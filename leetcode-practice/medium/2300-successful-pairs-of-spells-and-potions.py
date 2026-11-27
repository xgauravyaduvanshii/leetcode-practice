# LeetCode 2300. Successful Pairs of Spells and Potions — Medium
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Submission 2200992927 — Accepted, Python3
#
# My thinking: once the potions are sorted, each spell
# only needs the first potion strong enough for it —
# everything from there on works too.

import bisect


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        n = len(potions)
        result = []
        for spell in spells:
            need = -(-success // spell)
            result.append(n - bisect.bisect_left(potions, need))
        return result
