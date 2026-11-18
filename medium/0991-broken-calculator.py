# LeetCode 991. Broken Calculator — Medium
# https://leetcode.com/problems/broken-calculator/
# Submission 2198982932 — Accepted, Python3
#
# My thinking: working backwards is easier — from
# the target, halving is free in reverse and
# adding one is cheap. When the target drops to
# the start value or below, I just subtract down.

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            steps += 1
        return steps + startValue - target
