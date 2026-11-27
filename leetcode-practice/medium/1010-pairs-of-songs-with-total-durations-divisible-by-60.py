# LeetCode 1010. Pairs of Songs With Total Durations Divisible by 60 — Medium
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Submission 2198986108 — Accepted, Python3
#
# My thinking: only the remainder after dividing
# by 60 matters. For each song I count how many
# earlier songs have the remainder that completes
# it to a multiple of 60, then I record its own
# remainder.

from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = [0] * 60
        pairs = 0
        for t in time:
            pairs += counts[(60 - t % 60) % 60]
            counts[t % 60] += 1
        return pairs
