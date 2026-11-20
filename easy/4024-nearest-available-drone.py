# 4024. Nearest Available Drone (Easy)
# https://leetcode.com/problems/nearest-available-drone/
# Submission 2200098168 — Accepted, Python3
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        # My thinking: I measure how far each drone
        # is from the target, keep only the ones that
        # can actually reach it, and take the nearest
        # — the smallest index wins a tie.
        tx, ty = target
        best = -1
        best_dist = None
        for i, (x, y, r) in enumerate(drones):
            d = abs(x - tx) + abs(y - ty)
            if d <= r and (best_dist is None or d < best_dist):
                best = i
                best_dist = d
        return best
