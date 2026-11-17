# LeetCode 2515. Shortest Distance to Target String in a Circular Array — Easy
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
# Submission 2197796994 — Accepted, Python3
#
# My thinking: for each position holding the target
# word, the distance is the shorter way around the
# circle — either straight across or wrapping
# around. I take the smallest over all matches; if
# the target never appears, the answer is -1.
# Note: LeetCode's stub spells the method
# "closetTarget" but its test driver calls
# "closestTarget" — the submitted method is named
# closestTarget.

class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        best = -1
        for i, w in enumerate(words):
            if w == target:
                d = abs(i - startIndex)
                d = min(d, n - d)
                if best == -1 or d < best:
                    best = d
        return best
