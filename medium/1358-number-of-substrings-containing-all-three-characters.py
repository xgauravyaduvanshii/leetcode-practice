# LeetCode 1358. Number of Substrings Containing All Three Characters — Medium
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Submission 2199038344 — Accepted, Python3
#
# My thinking: for each end position, the
# earliest start that still holds all three
# letters is one past the oldest of their last
# appearances. Every start up to that point
# works.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {"a": -1, "b": -1, "c": -1}
        total = 0
        for i, ch in enumerate(s):
            last[ch] = i
            total += min(last.values()) + 1
        return total
