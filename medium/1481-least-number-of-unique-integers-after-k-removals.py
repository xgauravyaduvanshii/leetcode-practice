# LeetCode 1481. Least Number of Unique Integers after K Removals — Medium
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# Submission 2199859662 — Accepted, Python3
#
# My thinking: to kill off whole numbers I
# start with the rarest. Removing a number's
# full count erases it; I spend k on the
# smallest counts first.

from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted(Counter(arr).values())
        unique = len(counts)
        for count in counts:
            if k >= count:
                k -= count
                unique -= 1
            else:
                break
        return unique
