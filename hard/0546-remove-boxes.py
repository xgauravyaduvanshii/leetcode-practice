# LeetCode 546. Remove Boxes — Hard
# https://leetcode.com/problems/remove-boxes/
# Submission 2198662649 — Accepted, Python3
#
# My thinking: I look at a stretch of boxes plus some
# extra boxes of the same colour already attached to
# its front. Either I remove that front block now and
# take its squared score, or I keep it and merge it
# with a matching box further along, which makes the
# block bigger before I remove it.

from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def best(left, right, extra):
            if left > right:
                return 0
            end = left
            while end + 1 <= right and boxes[end + 1] == boxes[left]:
                end += 1
            extra += end - left
            score = (extra + 1) ** 2 + best(end + 1, right, 0)
            for middle in range(end + 1, right + 1):
                if boxes[middle] == boxes[left]:
                    score = max(
                        score,
                        best(end + 1, middle - 1, 0) + best(middle, right, extra + 1),
                    )
            return score

        return best(0, len(boxes) - 1, 0)
