# LeetCode 1218. Longest Arithmetic Subsequence of Given Difference — Medium
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
# Submission 2199012963 — Accepted, Python3
#
# My thinking: for each number I look up the
# best chain ending at the number one step
# behind it, and extend it by one. The longest
# chain I ever see is the answer.

from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lengths = {}
        best = 0
        for value in arr:
            lengths[value] = lengths.get(value - difference, 0) + 1
            best = max(best, lengths[value])
        return best
