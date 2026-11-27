# LeetCode 667. Beautiful Arrangement II — Medium
# https://leetcode.com/problems/beautiful-arrangement-ii/
# Submission 2198906387 — Accepted, Python3
#
# My thinking: I keep the first numbers in order so
# their gaps are all one, then alternate between
# the low and high ends of what is left — each
# swing makes a new larger gap, exactly k of them
# in total.

from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = list(range(1, n - k))
        low, high = n - k, n
        for i in range(k + 1):
            if i % 2 == 0:
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        return result
