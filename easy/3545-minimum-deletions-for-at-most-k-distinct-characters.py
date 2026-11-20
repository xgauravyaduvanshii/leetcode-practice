# 3545. Minimum Deletions for At Most K Distinct Characters (Easy)
# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/
# Submission 2200027266 — Accepted, Python3
from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        # My thinking: to keep at most k different
        # letters, I drop the rarest ones entirely.
        # Deleting a whole letter costs its full count,
        # so I start with the smallest counts.
        freqs = sorted(Counter(s).values())
        return sum(freqs[:max(0, len(freqs) - k)])
