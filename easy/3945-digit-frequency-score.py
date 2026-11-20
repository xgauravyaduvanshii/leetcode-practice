# 3945. Digit Frequency Score (Easy)
# https://leetcode.com/problems/digit-frequency-score/
# Submission 2200089902 — Accepted, Python3
from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # My thinking: each digit contributes itself
        # times how often it appears — so I add up
        # digit times count for every digit in the
        # number.
        return sum(d * c for d, c in Counter(int(ch) for ch in str(n)).items())
