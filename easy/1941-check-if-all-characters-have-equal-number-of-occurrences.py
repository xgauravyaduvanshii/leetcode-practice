# LeetCode 1941. Check if All Characters Have Equal Number of Occurrences — Easy
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
# Submission 2197604853 — Accepted, Python3
#
# My thinking: I count how many times each character
# appears. If all the counts are the same — that is,
# the set of counts has just one value — the answer
# is true.

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        return len(set(counts.values())) == 1
