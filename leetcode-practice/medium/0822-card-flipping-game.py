# LeetCode 822. Card Flipping Game — Medium
# https://leetcode.com/problems/card-flipping-game/
# Submission 2198947851 — Accepted, Python3
#
# My thinking: a number showing on both sides of
# one card is forced face up forever. Any other
# number that appears on either side can be
# flipped down, so the smallest such number wins.

from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        forced = {front for front, back in zip(fronts, backs) if front == back}
        candidates = [num for num in set(fronts) | set(backs) if num not in forced]
        return min(candidates, default=0)
