# LeetCode 710. Random Pick with Blacklist — Hard
# https://leetcode.com/problems/random-pick-with-blacklist/
# Submission 2198668637 — Accepted, Python3
#
# My thinking: only n minus the blacklist size numbers
# are pickable, so I roll in that smaller range. A
# blacklisted number below the range is remapped to a
# free number from the top end, which no roll can land
# on directly — every pick stays uniform and valid.

import random
from typing import List


class RandomPickWithBlacklist:
    def __init__(self, n: int, blacklist: List[int]):
        self.size = n - len(blacklist)
        black = set(blacklist)
        self.mapping = {}
        last = n - 1
        for b in blacklist:
            if b < self.size:
                while last in black:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        roll = random.randint(0, self.size - 1)
        return self.mapping.get(roll, roll)
