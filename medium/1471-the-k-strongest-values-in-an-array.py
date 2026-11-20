# LeetCode 1471. The k Strongest Values in an Array — Medium
# https://leetcode.com/problems/the-k-strongest-values-in-an-array/
# Submission 2199857232 — Accepted, Python3
#
# My thinking: strength is distance from the
# median, with the bigger value winning a tie.
# I sort by that rule and take the first k.

from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)
        return arr[:k]
