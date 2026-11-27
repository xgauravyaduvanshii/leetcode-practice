# 3940. Limit Occurrences in Sorted Array (Easy)
# https://leetcode.com/problems/limit-occurrences-in-sorted-array/
# Submission 2200089473 — Accepted, Python3
from collections import Counter


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        # My thinking: I walk the sorted array keeping
        # a count per value, and drop any copy past
        # the k-th one.
        counts = Counter()
        out = []
        for x in nums:
            if counts[x] < k:
                out.append(x)
                counts[x] += 1
        return out
