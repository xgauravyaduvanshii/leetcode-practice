# 3178. Find the Child Who Has the Ball After K Seconds (Easy)
# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/
# Submission 2199983835 — Accepted, Python3
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # My thinking: the ball goes back and forth along
        # the line, so its trip repeats every two passes
        # minus the ends. Where it is after k seconds is
        # just k inside one repeat, folded back if it is
        # on the way back.
        cycle = 2 * (n - 1)
        step = k % cycle
        if step < n:
            return step
        return cycle - step
