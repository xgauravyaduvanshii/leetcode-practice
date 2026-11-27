# LeetCode 657. Robot Return to Origin — Easy
# https://leetcode.com/problems/robot-return-to-origin/
# Submission 2197510671 — Accepted, Python3
#
# My thinking: the robot ends up back where it
# started exactly when it moved up as many times
# as down, and left as many times as right. So I
# just count each direction and compare the pairs.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
