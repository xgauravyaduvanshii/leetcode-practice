# LeetCode 522. Longest Uncommon Subsequence II — Medium
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/
# Submission 2198844428 — Accepted, Python3
#
# My thinking: if a string is a subsequence of
# another one, it can never be uncommon. So I only
# need to check the strings themselves, longest
# first — the first one that is nobody else's
# subsequence is the answer.

from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(short, long):
            i = 0
            for char in long:
                if i < len(short) and short[i] == char:
                    i += 1
            return i == len(short)

        strs.sort(key=len, reverse=True)
        for i, candidate in enumerate(strs):
            if all(
                i == j or not is_subsequence(candidate, other)
                for j, other in enumerate(strs)
            ):
                return len(candidate)
        return -1
