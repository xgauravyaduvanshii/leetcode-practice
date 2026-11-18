# LeetCode 756. Pyramid Transition Matrix — Medium
# https://leetcode.com/problems/pyramid-transition-matrix/
# Submission 2198930179 — Accepted, Python3
#
# My thinking: I build the pyramid one row at a
# time, trying every allowed block for each pair
# below. Memoised depth-first search remembers
# which rows can still finish, so the same row is
# never retried.

from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        rules = {}
        for triple in allowed:
            rules.setdefault(triple[:2], []).append(triple[2])

        def can_build(row, above, index, memo):
            if len(row) == 1:
                return True
            if index == len(row) - 1:
                return can_build(above, "", 0, memo)
            key = (row, above, index)
            if key in memo:
                return memo[key]
            for next_block in rules.get(row[index:index + 2], []):
                if can_build(row, above + next_block, index + 1, memo):
                    memo[key] = True
                    return True
            memo[key] = False
            return False

        return can_build(bottom, "", 0, {})
