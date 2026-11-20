# 3467. Transform Array by Parity (Easy)
# https://leetcode.com/problems/transform-array-by-parity/
# Submission 2200019870 — Accepted, Python3
from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # My thinking: every even number becomes 0 and
        # every odd number becomes 1, then the zeroes
        # all move to the front. Sorting the transformed
        # array does exactly that.
        return sorted(num % 2 for num in nums)
