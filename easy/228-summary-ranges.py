# 228. Summary Ranges (Easy)
# https://leetcode.com/problems/summary-ranges/
# Submission 2199957346 — Accepted, Python3
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # My thinking: walk the numbers once, keeping the
        # start of the current run. A run ends when the
        # next number is not one bigger — then I write it
        # down as a single number or as start->end.
        ranges = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{end}")
            i += 1
        return ranges
