# LeetCode 2224. Minimum Number of Operations to Convert Time — Easy
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/
# Submission 2197618563 — Accepted, Python3
#
# My thinking: I convert both times to minutes and
# take the difference. Then I use the biggest steps
# first — 60, 15, 5, then 1 — which is greedy and
# optimal for these step sizes.

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def to_minutes(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)
        diff = to_minutes(correct) - to_minutes(current)
        ops = 0
        for d in (60, 15, 5, 1):
            ops += diff // d
            diff %= d
        return ops
