# 3560. Find Minimum Log Transportation Cost (Easy)
# https://leetcode.com/problems/find-minimum-log-transportation-cost/
# Submission 2200028432 — Accepted, Python3
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        # My thinking: two logs, three trucks, each
        # truck holds one piece of length at most k.
        # A log that already fits costs nothing. A log
        # longer than k must be cut once — into a piece
        # of length k and the rest — and that cut costs
        # k times the leftover. At most one log can be
        # too long, since the input always fits.
        longest = max(n, m)
        if longest <= k:
            return 0
        return k * (longest - k)
