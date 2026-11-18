# LeetCode 950. Reveal Cards In Increasing Order — Medium
# https://leetcode.com/problems/reveal-cards-in-increasing-order/
# Submission 2198975696 — Accepted, Python3
#
# My thinking: I work backwards from the answer.
# The smallest card goes first, then I put the
# next card at the front of the line and move
# the card behind it to the back — exactly the
# reverse of how the cards are revealed.

from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque(range(len(deck)))
        result = [0] * len(deck)
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return result
