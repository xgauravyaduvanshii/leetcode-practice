# 3432. Count Partitions With Even Sum Difference (Easy)
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/
# Submission 2200015435 — Accepted, Python3
from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # My thinking: the difference between the two
        # sides is even exactly when the whole array's
        # sum is even — the left part cancels out. So
        # either every split counts, or none does.
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0
