# 2778. Sum of Squares of Special Elements (Easy)
# https://leetcode.com/problems/sum-of-squares-of-special-elements/
# Submission 2199969853 — Accepted, Python3
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # My thinking: an element is special when its
        # one-based position divides the length of the
        # list. I add the square of each special element
        # and skip the rest.
        n = len(nums)
        total = 0
        for i, num in enumerate(nums, start=1):
            if n % i == 0:
                total += num * num
        return total
