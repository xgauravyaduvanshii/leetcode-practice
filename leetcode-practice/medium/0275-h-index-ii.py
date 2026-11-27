# LeetCode 275. H-Index II — Medium
# https://leetcode.com/problems/h-index-ii/
# Submission 2198727711 — Accepted, Python3
#
# My thinking: the citations are already sorted, so
# I binary-search for the first position where the
# citation count is at least the number of papers
# from there on. That count is the h-index.

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                answer = n - mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
