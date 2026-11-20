# 3861. Minimum Capacity Box (Easy)
# https://leetcode.com/problems/minimum-capacity-box/
# Submission 2200077952 — Accepted, Python3
class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        # My thinking: among the boxes big enough for
        # the item, the smallest capacity wins — and
        # if several share it, the earliest box wins.
        best = -1
        for i, c in enumerate(capacity):
            if c >= itemSize and (best == -1 or c < capacity[best]):
                best = i
        return best
