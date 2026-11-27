# 3684. Maximize Sum of At Most K Distinct Elements (Easy)
# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/
# Submission 2200043354 — Accepted, Python3
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # My thinking: I can pick at most k different
        # numbers, so I take the k biggest distinct
        # ones — or all of them if there are fewer —
        # and add them up.
        return sum(sorted(set(nums), reverse=True)[:k])
