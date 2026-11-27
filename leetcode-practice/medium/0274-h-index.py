# LeetCode 274. H-Index — Medium
# https://leetcode.com/problems/h-index/
# Submission 2198727211 — Accepted, Python3
#
# My thinking: after sorting, a paper at position i
# has n - i papers at least as cited as it. The
# first position where the citation count reaches
# that many papers gives the h-index.

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i, citation in enumerate(citations):
            if citation >= n - i:
                return n - i
        return 0
