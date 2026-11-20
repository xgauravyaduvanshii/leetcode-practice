# 3074. Apple Redistribution into Boxes (Easy)
# https://leetcode.com/problems/apple-redistribution-into-boxes/
# Submission 2199973712 — Accepted, Python3
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # My thinking: count all the apples, then take
        # the biggest boxes first — each box taken adds
        # its room, and I stop as soon as the room taken
        # covers all the apples.
        total = sum(apple)
        capacity.sort(reverse=True)
        used = 0
        boxes = 0
        for room in capacity:
            used += room
            boxes += 1
            if used >= total:
                return boxes
        return boxes
