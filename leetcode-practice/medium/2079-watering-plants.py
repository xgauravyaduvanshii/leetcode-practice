# LeetCode 2079. Watering Plants — Medium
# https://leetcode.com/problems/watering-plants/
# Submission 2204400645 — Accepted, Python3
#
# My thinking: I walk the plants left to right with a full can. When
# the water left is less than the next plant needs, I walk back to the
# river and out again, which costs twice the plant's index in steps,
# then refill. Every plant also costs one step to reach, so I add one
# per plant and subtract what it drinks.
class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        steps = 0
        cur = capacity
        for i, need in enumerate(plants):
            if cur < need:
                steps += 2 * i
                cur = capacity
            steps += 1
            cur -= need
        return steps
