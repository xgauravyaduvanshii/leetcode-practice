# 3516. Find Closest Person (Easy)
# https://leetcode.com/problems/find-closest-person/
# Submission 2200026229 — Accepted, Python3
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # My thinking: compare how far each person is
        # from z. The nearer one reaches z first — and
        # if they are equally far, neither does.
        dx = abs(x - z)
        dy = abs(y - z)
        if dx < dy:
            return 1
        if dy < dx:
            return 2
        return 0
