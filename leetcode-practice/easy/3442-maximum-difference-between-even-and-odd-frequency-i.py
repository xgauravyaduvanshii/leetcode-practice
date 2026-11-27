# 3442. Maximum Difference Between Even and Odd Frequency I (Easy)
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
# Submission 2200016082 — Accepted, Python3
from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        # My thinking: count every character. The
        # answer is the biggest odd count minus the
        # smallest even count — the odd side wants to
        # be as large as possible and the even side as
        # small as possible.
        counts = Counter(s).values()
        odd = max(c for c in counts if c % 2 == 1)
        even = min(c for c in counts if c % 2 == 0)
        return odd - even
