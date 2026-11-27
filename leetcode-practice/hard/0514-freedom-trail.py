# LeetCode 514. Freedom Trail — Hard
# https://leetcode.com/problems/freedom-trail/
# Submission 2198661590 — Accepted, Python3
#
# My thinking: for each letter of the key I keep the
# cheapest cost to reach every spot on the ring that
# holds that letter. Moving between two spots costs
# the shorter way round the ring, and the button press
# adds one per letter at the very end.

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        spots = {}
        for i, char in enumerate(ring):
            spots.setdefault(char, []).append(i)

        cost = {0: 0}
        for char in key:
            next_cost = {}
            for spot in spots[char]:
                best = min(
                    previous_cost
                    + min(abs(spot - prev), len(ring) - abs(spot - prev))
                    for prev, previous_cost in cost.items()
                )
                next_cost[spot] = best
            cost = next_cost
        return min(cost.values()) + len(key)
