# LeetCode 1560. Most Visited Sector in a Circular Track — Easy
# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
# Submission 2197585943 — Accepted, Python3
#
# My thinking: I simulate the laps sector by sector,
# counting how many times each sector is visited
# as the runner moves from one round's end to the
# next. Then I return every sector that ties for
# the highest visit count.

class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        visits = [0] * (n + 1)
        current = rounds[0]
        visits[current] += 1
        for target in rounds[1:]:
            while current != target:
                current = current % n + 1
                visits[current] += 1
        most = max(visits)
        return [i for i in range(1, n + 1) if visits[i] == most]
