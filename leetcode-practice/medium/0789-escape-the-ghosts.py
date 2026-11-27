# LeetCode 789. Escape The Ghosts — Medium
# https://leetcode.com/problems/escape-the-ghosts/
# Submission 2198938131 — Accepted, Python3
#
# My thinking: ghosts and I both move one step at
# a time, so only distances matter. I escape when
# I reach the target strictly before every ghost
# could get there.

from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_steps = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            if abs(gx - target[0]) + abs(gy - target[1]) <= my_steps:
                return False
        return True
