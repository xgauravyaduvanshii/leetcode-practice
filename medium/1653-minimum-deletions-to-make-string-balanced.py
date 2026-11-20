# LeetCode 1653. Minimum Deletions to Make String Balanced — Medium
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# Submission 2199901553 — Accepted, Python3
#
# My thinking: a balanced string is some a's
# then some b's. Reading left to right, every
# a that follows a b must go — or one of those
# b's must. I delete whichever is cheaper as
# I go.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletions = 0
        for ch in s:
            if ch == "b":
                b_count += 1
            elif b_count > 0:
                deletions += 1
                b_count -= 1
        return deletions
