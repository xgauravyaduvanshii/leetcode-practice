# LeetCode 2126. Destroying Asteroids — Medium
# https://leetcode.com/problems/destroying-asteroids/
# Submission 2204409264 — Accepted, Python3
#
# My thinking: to survive, the planet must absorb the asteroids from
# smallest to largest — taking a big one early can only help if the
# smaller ones are already absorbed, and the mass only grows. So I
# sort them and check in order that the current mass is at least each
# asteroid, adding its mass as I go.
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        for a in sorted(asteroids):
            if mass < a:
                return False
            mass += a
        return True
