# 3663. Find the Least Frequent Digit (Easy)
# https://leetcode.com/problems/find-the-least-frequent-digit/
# Submission 2200038606 — Accepted, Python3
from collections import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        # My thinking: count how often each digit of
        # the number appears. The rarest one wins, and
        # if several tie, the smallest digit wins — and
        # the answer comes back as a number, not a
        # character.
        counts = Counter(str(n))
        return int(min(counts, key=lambda d: (counts[d], int(d))))
