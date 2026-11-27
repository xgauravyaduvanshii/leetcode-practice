# LeetCode 833. Find And Replace in String — Medium
# https://leetcode.com/problems/find-and-replace-in-string/
# Submission 2198949401 — Accepted, Python3
#
# My thinking: I only replace where the source
# actually matches at that index. Working from
# the end backwards keeps the earlier indices
# untouched, so each replacement lands exactly
# where it should.

from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        result = list(s)
        for index, source, target in sorted(zip(indices, sources, targets), reverse=True):
            if s[index:index + len(source)] == source:
                result[index:index + len(source)] = list(target)
        return "".join(result)
