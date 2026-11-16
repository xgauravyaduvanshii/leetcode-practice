# LeetCode 1732. Find the Highest Altitude — Easy
# https://leetcode.com/problems/find-the-highest-altitude/
# Submission 2197595756 — Accepted, Python3
#
# My thinking: I walk the gains adding them up to
# track the current altitude, starting from 0.
# The highest altitude I ever reach is the answer.

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        best = 0
        for g in gain:
            altitude += g
            best = max(best, altitude)
        return best
