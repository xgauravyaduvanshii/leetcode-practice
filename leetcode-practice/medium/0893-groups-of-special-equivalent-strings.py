# LeetCode 893. Groups of Special-Equivalent Strings — Medium
# https://leetcode.com/problems/groups-of-special-equivalent-strings/
# Submission 2198965081 — Accepted, Python3
#
# My thinking: swapping letters only moves them
# within even or odd positions, never across. So
# two words are equivalent exactly when their
# even-position letters and odd-position letters
# match as sorted groups.

from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        for word in words:
            even = tuple(sorted(word[0::2]))
            odd = tuple(sorted(word[1::2]))
            groups.add((even, odd))
        return len(groups)
