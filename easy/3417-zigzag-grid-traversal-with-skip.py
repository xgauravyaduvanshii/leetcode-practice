# 3417. Zigzag Grid Traversal With Skip (Easy)
# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/
# Submission 2200014483 — Accepted, Python3
from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        # My thinking: walk the rows in a zigzag — left
        # to right, then right to left — and take every
        # other cell I visit, starting with the first.
        order = []
        for r, row in enumerate(grid):
            if r % 2 == 0:
                order.extend(row)
            else:
                order.extend(reversed(row))
        return order[::2]
