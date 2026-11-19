# LeetCode 1423. Maximum Points You Can Obtain from Cards — Medium
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Submission 2199056214 — Accepted, Python3
#
# My thinking: taking k cards from the ends
# leaves a middle window I skip. The best take
# is the total minus the smallest window I can
# leave behind, so I slide that window along.

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window = sum(cardPoints[:n - k])
        best = total - window
        for i in range(n - k, n):
            window += cardPoints[i] - cardPoints[i - (n - k)]
            best = max(best, total - window)
        return best
