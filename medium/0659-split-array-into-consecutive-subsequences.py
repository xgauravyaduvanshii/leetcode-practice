# LeetCode 659. Split Array into Consecutive Subsequences — Medium
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Submission 2198901502 — Accepted, Python3
#
# My thinking: I walk the numbers in order. Each
# one either continues a subsequence that is
# waiting for it, or starts a fresh one of length
# three. If neither is possible, the split fails.

from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        available = Counter(nums)
        tails = Counter()
        for num in nums:
            if available[num] == 0:
                continue
            available[num] -= 1
            if tails[num - 1] > 0:
                tails[num - 1] -= 1
                tails[num] += 1
            elif available[num + 1] > 0 and available[num + 2] > 0:
                available[num + 1] -= 1
                available[num + 2] -= 1
                tails[num + 2] += 1
            else:
                return False
        return True
