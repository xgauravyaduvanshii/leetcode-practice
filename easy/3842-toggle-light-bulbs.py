# 3842. Toggle Light Bulbs (Easy)
# https://leetcode.com/problems/toggle-light-bulbs/
# Submission 2200072510 — Accepted, Python3
from collections import Counter


class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        # My thinking: a bulb ends up on exactly when
        # it gets toggled an odd number of times. I
        # count the toggles and keep the bulbs with an
        # odd count, in order.
        counts = Counter(bulbs)
        return sorted(b for b, c in counts.items() if c % 2 == 1)
