# 1861. Rotating the Box (Medium)
# https://leetcode.com/problems/rotating-the-box/
# Submission 2199951147 — Accepted, Python3
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # My thinking: first turn the box 90 degrees
        # clockwise, then let gravity do its work. After
        # the turn, the old right edge is the new floor,
        # so in the rotated box every stone falls straight
        # down its column until it hits an obstacle or
        # another stone. Each column is settled by
        # scanning it from the bottom up.
        rows, cols = len(box), len(box[0])
        rotated = [[""] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated[j][rows - 1 - i] = box[i][j]
        for c in range(rows):
            # write marks where the next falling stone lands.
            write = cols - 1
            for i in range(cols - 1, -1, -1):
                if rotated[i][c] == "*":
                    write = i - 1
                elif rotated[i][c] == "#":
                    rotated[write][c] = "#"
                    if write != i:
                        rotated[i][c] = "."
                    write -= 1
        return rotated
