# LeetCode 2582. Pass the Pillow — Easy
# https://leetcode.com/problems/pass-the-pillow/
# Submission 2197806437 — Accepted, Python3
#
# My thinking: the pillow goes back and forth, so
# the motion repeats every 2*(n-1) seconds. Within
# one cycle, it moves forward for the first n-1
# seconds and back for the rest.

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2 * (n - 1)
        t = time % cycle
        if t < n:
            return t + 1
        return 2 * n - 1 - t
