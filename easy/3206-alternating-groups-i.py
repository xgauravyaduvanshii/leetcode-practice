# 3206. Alternating Groups I (Easy)
# https://leetcode.com/problems/alternating-groups-i/
# Submission 2199985219 — Accepted, Python3
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        # My thinking: a tile sits in the middle of an
        # alternating group when both its neighbours are
        # the opposite colour. The circle wraps around,
        # so the first and last tiles are neighbours too.
        n = len(colors)
        count = 0
        for i in range(n):
            if colors[i - 1] != colors[i] and colors[i] != colors[(i + 1) % n]:
                count += 1
        return count
