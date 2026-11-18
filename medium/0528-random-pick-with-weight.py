# LeetCode 528. Random Pick with Weight — Medium
# https://leetcode.com/problems/random-pick-with-weight/
# Submission 2198849377 — Accepted, Python3
#
# My thinking: I lay the weights out end to end as
# running totals, then draw a random number in that
# range — the index it lands on is picked with
# probability matching its weight.

import bisect
import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])
        return bisect.bisect_left(self.prefix, target)
