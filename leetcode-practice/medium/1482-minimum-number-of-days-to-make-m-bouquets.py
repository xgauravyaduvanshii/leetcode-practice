# LeetCode 1482. Minimum Number of Days to Make m Bouquets — Medium
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
# Submission 2199859959 — Accepted, Python3
#
# My thinking: if a day works, every later day
# works too — so I binary-search the earliest
# day with enough bouquets. A day works when
# the bloomed flowers form m groups of k in a
# row.

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def can_make(days):
            bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        low, high = 1, max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if can_make(mid):
                high = mid
            else:
                low = mid + 1
        return low
