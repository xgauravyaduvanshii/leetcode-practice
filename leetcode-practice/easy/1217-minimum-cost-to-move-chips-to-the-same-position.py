# LeetCode 1217. Minimum Cost to Move Chips to The Same Position — Easy
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# Submission 2197563497 — Accepted, Python3
#
# My thinking: moving a chip by 2 is free, so only
# parity matters — a chip can reach any position
# of the same parity for free. So I just count the
# chips on odd positions and the chips on even
# positions, and move whichever group is smaller.

class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        odd = sum(p % 2 for p in position)
        return min(odd, len(position) - odd)
