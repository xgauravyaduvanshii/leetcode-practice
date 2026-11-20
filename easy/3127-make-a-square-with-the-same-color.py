# 3127. Make a Square with the Same Color (Easy)
# https://leetcode.com/problems/make-a-square-with-the-same-color/
# Submission 2199978622 — Accepted, Python3
from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        # My thinking: changing one cell can only fix a
        # 2 by 2 block that already has three of the same
        # colour. So I check every 2 by 2 block for three
        # B's or three W's.
        for r in range(2):
            for c in range(2):
                block = [grid[r][c], grid[r][c + 1], grid[r + 1][c], grid[r + 1][c + 1]]
                if block.count("B") >= 3 or block.count("W") >= 3:
                    return True
        return False
