# 3300. Minimum Element After Replacement With Digit Sum (Easy)
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
# Submission 2200002325 — Accepted, Python3
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        # My thinking: replace each number by the sum of
        # its digits, then take the smallest of those
        # sums.
        return min(sum(int(d) for d in str(num)) for num in nums)
