# 3798. Largest Even Number (Easy)
# https://leetcode.com/problems/largest-even-number/
# Submission 2200066915 — Accepted, Python3
class Solution:
    def largestEven(self, s: str) -> str:
        # My thinking: an even number must end in 2,
        # and a longer number beats a shorter one. So
        # I keep everything up to the last 2 in the
        # string — and if there is no 2 at all, there
        # is no even number to make.
        last = s.rfind("2")
        return s[:last + 1] if last != -1 else ""
