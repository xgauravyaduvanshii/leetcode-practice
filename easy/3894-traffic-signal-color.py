# 3894. Traffic Signal Color (Easy)
# https://leetcode.com/problems/traffic-signal-color/
# Submission 2200084771 — Accepted, Python3
class Solution:
    def trafficSignal(self, timer: int) -> str:
        # My thinking: the signal is green at zero,
        # orange at exactly thirty, red from thirty-one
        # to ninety — anything else is invalid.
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if 30 < timer <= 90:
            return "Red"
        return "Invalid"
