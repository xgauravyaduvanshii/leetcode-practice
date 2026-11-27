# 4070. Minimum Rotations to Dial a Number I (Easy)
# https://leetcode.com/problems/minimum-rotations-to-dial-a-number-i/
# Submission 2200102526 — Accepted, Python3
class Solution:
    def minRotations(self, s: str) -> int:
        # My thinking: the dial is circular, so the
        # cheapest hop between two digits is the
        # shorter way round — never more than five
        # steps. I add up the hops from zero onwards.
        total = 0
        cur = 0
        for ch in s:
            d = int(ch)
            total += min(abs(d - cur), 10 - abs(d - cur))
            cur = d
        return total
