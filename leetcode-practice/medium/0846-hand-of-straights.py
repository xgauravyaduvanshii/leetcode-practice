# LeetCode 846. Hand of Straights — Medium
# https://leetcode.com/problems/hand-of-straights/
# Submission 2198953275 — Accepted, Python3
#
# My thinking: I always start a group at the
# smallest card left — it has nowhere else to
# go. If any card in the run is missing, the
# hand cannot be split.

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        for card in sorted(counts):
            while counts[card] > 0:
                for next_card in range(card, card + groupSize):
                    if counts[next_card] == 0:
                        return False
                    counts[next_card] -= 1
        return True
