# LeetCode 2212. Maximum Points in an Archery Competition — Medium
# https://leetcode.com/problems/maximum-points-in-an-archery-competition/
# Submission 2204502305 — Accepted, Python3
#
# My thinking: there are only 12 scoring sections, so I try every
# subset of sections to win, keeping the one with the highest points
# whose arrow cost fits in the budget. Winning a section costs one more
# arrow than Alice used there, and any arrows left over are dumped into
# section 0 where they change nothing.
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        best_points = -1
        best_mask = 0
        for mask in range(1 << 12):
            cost = 0
            points = 0
            for i in range(12):
                if (mask >> i) & 1:
                    cost += aliceArrows[i] + 1
                    points += i
            if cost <= numArrows and points > best_points:
                best_points = points
                best_mask = mask
        bob = [0] * 12
        used = 0
        for i in range(12):
            if (best_mask >> i) & 1:
                bob[i] = aliceArrows[i] + 1
                used += bob[i]
        bob[0] += numArrows - used
        return bob
