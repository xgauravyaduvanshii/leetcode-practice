# LeetCode 1876. Substrings of Size Three with Distinct Characters — Easy
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# Submission 2197602427 — Accepted, Python3
#
# My thinking: I slide a window of three characters
# across the string and count the windows where all
# three characters are different.

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(1 for i in range(len(s) - 2) if len({s[i], s[i + 1], s[i + 2]}) == 3)
