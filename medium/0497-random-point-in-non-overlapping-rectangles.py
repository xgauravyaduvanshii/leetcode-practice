# LeetCode 497. Random Point in Non-overlapping Rectangles — Medium
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# Submission 2198831340 — Accepted, Python3
#
# My thinking: a bigger rectangle deserves more
# picks, so I line the rectangles up by their area
# and pick one with a weighted random draw. Then I
# choose a random point inside that rectangle.

import bisect
import random
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0
        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)

    def pick(self) -> List[int]:
        target = random.randint(1, self.prefix[-1])
        index = bisect.bisect_left(self.prefix, target)
        x1, y1, x2, y2 = self.rects[index]
        return [random.randint(x1, x2), random.randint(y1, y2)]
