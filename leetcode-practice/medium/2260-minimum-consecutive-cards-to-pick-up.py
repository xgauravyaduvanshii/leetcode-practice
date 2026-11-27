# LeetCode 2260. Minimum Consecutive Cards to Pick Up — Medium
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
# Submission 2204519077 — Accepted, Python3
#
# My thinking: any valid pick-up must contain two equal cards, and the
# shortest one for a value is between two consecutive occurrences of
# it. I scan once, remembering the last position of each value, and
# keep the smallest distance between repeats; if no value repeats, the
# answer is -1.
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        last = {}
        ans = float('inf')
        for i, c in enumerate(cards):
            if c in last:
                ans = min(ans, i - last[c] + 1)
            last[c] = i
        return ans if ans != float('inf') else -1
