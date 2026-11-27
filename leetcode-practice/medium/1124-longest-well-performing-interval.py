# LeetCode 1124. Longest Well-Performing Interval — Medium
# https://leetcode.com/problems/longest-well-performing-interval/
# Submission 2199002003 — Accepted, Python3
#
# My thinking: I score each day plus one for a
# long day and minus one otherwise. A stretch
# is well-performing when its total score is
# positive, so I look back to the first time
# the score was one less than it is now.

from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score = 0
        first_seen = {0: -1}
        best = 0
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            if score > 0:
                best = i + 1
            elif score - 1 in first_seen:
                best = max(best, i - first_seen[score - 1])
            if score not in first_seen:
                first_seen[score] = i
        return best
