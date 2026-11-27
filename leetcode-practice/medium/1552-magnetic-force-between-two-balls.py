# LeetCode 1552. Magnetic Force Between Two Balls — Medium
# https://leetcode.com/problems/magnetic-force-between-two-balls/
# Submission 2199875230 — Accepted, Python3
#
# My thinking: if a gap works, every smaller
# gap works too — so I binary-search the
# biggest workable gap, greedily placing balls
# as far apart as that gap allows.

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(min_dist):
            placed = 1
            last = position[0]
            for pos in position[1:]:
                if pos - last >= min_dist:
                    placed += 1
                    last = pos
                    if placed == m:
                        return True
            return False

        low, high = 1, position[-1] - position[0]
        while low < high:
            mid = (low + high + 1) // 2
            if can_place(mid):
                low = mid
            else:
                high = mid - 1
        return low
