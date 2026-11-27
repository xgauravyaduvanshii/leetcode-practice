# 3477. Fruits Into Baskets II (Easy)
# https://leetcode.com/problems/fruits-into-baskets-ii/
# Submission 2200020503 — Accepted, Python3
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # My thinking: take each fruit in order and put
        # it in the first basket from the left that is
        # big enough. A basket can hold only one fruit,
        # so once used it is gone. Whatever is left
        # without a basket stays unplaced.
        unplaced = 0
        for fruit in fruits:
            placed = False
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets[i] = 0
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced
