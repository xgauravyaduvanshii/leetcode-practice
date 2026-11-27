# LeetCode 2839. Check if Strings Can be Made Equal With Operations I — Easy
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
# Submission 2198419401 — Accepted, Python3
#
# My thinking: a swap can only move a character two
# places, so characters on even positions can only
# trade with even positions, and odd with odd. The
# strings can match exactly when the letters at the
# even spots agree as a group and the letters at the
# odd spots agree as a group.

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1[0:4:2]) == sorted(s2[0:4:2]) and sorted(s1[1:4:2]) == sorted(s2[1:4:2])
