# LeetCode 777. Swap Adjacent in LR String — Medium
# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# Submission 2198932943 — Accepted, Python3
#
# My thinking: X's can be ignored, but the L's and
# R's must appear in the same order in both
# strings. L can only move left and R only right,
# so I check each letter's position against that
# rule.

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace("X", "") != result.replace("X", ""):
            return False
        i = j = 0
        while i < len(start) and j < len(result):
            while i < len(start) and start[i] == "X":
                i += 1
            while j < len(result) and result[j] == "X":
                j += 1
            if i == len(start) or j == len(result):
                break
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False
            i += 1
            j += 1
        return True
