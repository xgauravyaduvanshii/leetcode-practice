# LeetCode 2453. Destroy Sequential Targets — Medium
# https://leetcode.com/problems/destroy-sequential-targets/
# Submission 2204951337 — Accepted, Python3
#
# My thinking: choosing a first target destroys exactly the numbers
# sharing its remainder modulo space, so group the numbers by that
# remainder. The biggest group wins; ties go to the group holding
# the smallest number.
from collections import defaultdict


class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        groups = defaultdict(list)
        for x in nums:
            groups[x % space].append(x)
        best_count = 0
        best_val = None
        for vals in groups.values():
            if len(vals) > best_count:
                best_count = len(vals)
                best_val = min(vals)
            elif len(vals) == best_count:
                best_val = min(best_val, min(vals))
        return best_val
