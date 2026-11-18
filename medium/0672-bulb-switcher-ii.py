# LeetCode 672. Bulb Switcher II — Medium
# https://leetcode.com/problems/bulb-switcher-ii/
# Submission 2198907483 — Accepted, Python3
#
# My thinking: only the first three bulbs can ever
# look different, and each of the four switches
# flips a fixed pattern. So the number of states
# depends only on how many bulbs and presses there
# are, and it caps out at eight.

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        return 8
