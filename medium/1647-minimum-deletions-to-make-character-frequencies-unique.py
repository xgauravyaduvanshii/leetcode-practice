# LeetCode 1647. Minimum Deletions to Make Character Frequencies Unique — Medium
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# Submission 2199900674 — Accepted, Python3
#
# My thinking: I take the frequencies biggest
# first and shave each one down just until
# its count is not taken yet. Every shave is
# one deletion.

from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counts = sorted(Counter(s).values(), reverse=True)
        deletions = 0
        used = set()
        for count in counts:
            while count > 0 and count in used:
                count -= 1
                deletions += 1
            if count > 0:
                used.add(count)
        return deletions
