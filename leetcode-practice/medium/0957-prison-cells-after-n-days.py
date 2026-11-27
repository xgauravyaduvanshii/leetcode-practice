# LeetCode 957. Prison Cells After N Days — Medium
# https://leetcode.com/problems/prison-cells-after-n-days/
# Submission 2198976513 — Accepted, Python3
#
# My thinking: each day's cells come from their
# neighbours, and the pattern soon repeats. Once
# I see a state I have seen before, I know the
# cycle length and skip whole cycles at once.

from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        day = 0
        while day < n:
            state = tuple(cells)
            if state in seen:
                cycle = day - seen[state]
                remaining = (n - day) % cycle
                return self.prisonAfterNDays(cells, remaining)
            seen[state] = day
            cells = [0] + [1 if cells[i - 1] == cells[i + 1] else 0 for i in range(1, 7)] + [0]
            day += 1
        return cells
