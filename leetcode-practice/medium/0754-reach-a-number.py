# LeetCode 754. Reach a Number — Medium
# https://leetcode.com/problems/reach-a-number/
# Submission 2198929719 — Accepted, Python3
#
# My thinking: after n moves I have covered
# 1 + 2 + ... + n. I keep moving until that total
# reaches the target and the overshoot is even —
# then flipping one move lands exactly on it.

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        steps = 0
        total = 0
        while total < target or (total - target) % 2 != 0:
            steps += 1
            total += steps
        return steps
