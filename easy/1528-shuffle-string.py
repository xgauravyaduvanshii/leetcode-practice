# LeetCode 1528. Shuffle String — Easy
# https://leetcode.com/problems/shuffle-string/
# Submission 2197584424 — Accepted, Python3
#
# My thinking: the indices tell me where each
# character belongs. I make an empty list of the
# same length, place each character at its target
# position, and join it back into a string.

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [""] * len(s)
        for i, ch in enumerate(s):
            result[indices[i]] = ch
        return "".join(result)
