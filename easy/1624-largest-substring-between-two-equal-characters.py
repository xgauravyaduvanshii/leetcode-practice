# LeetCode 1624. Largest Substring Between Two Equal Characters — Easy
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/
# Submission 2197589961 — Accepted, Python3
#
# My thinking: for each character I remember where
# I first saw it. Every later sighting gives a
# candidate — the gap between the two positions
# minus one. The biggest gap wins; if no character
# repeats, the answer is -1.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        best = -1
        for i, ch in enumerate(s):
            if ch in first:
                best = max(best, i - first[ch] - 1)
            else:
                first[ch] = i
        return best
