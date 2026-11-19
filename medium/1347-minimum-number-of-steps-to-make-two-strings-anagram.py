# LeetCode 1347. Minimum Number of Steps to Make Two Strings Anagram — Medium
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# Submission 2199036803 — Accepted, Python3
#
# My thinking: I count how many of each letter
# the first string has over the second. Those
# extra letters are exactly the ones that must
# be swapped out.

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = Counter(s)
        counts.subtract(Counter(t))
        return sum(value for value in counts.values() if value > 0)
