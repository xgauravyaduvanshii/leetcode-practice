# LeetCode 1849. Splitting a String Into Descending Consecutive Values — Medium
# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
# Submission 2199947035 — Accepted, Python3
#
# My thinking: I try every possible first
# number, then backtrack through the rest —
# each next piece must be exactly one less
# than the last. A piece that grows past that
# target can never shrink, so I stop there.

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(index, previous):
            if index == len(s):
                return True
            for end in range(index + 1, len(s) + 1):
                value = int(s[index:end])
                if value == previous - 1 and backtrack(end, value):
                    return True
                if value > previous - 1:
                    break
            return False

        for end in range(1, len(s)):
            first = int(s[:end])
            if backtrack(end, first):
                return True
        return False
