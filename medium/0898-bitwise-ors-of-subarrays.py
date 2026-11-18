# LeetCode 898. Bitwise ORs of Subarrays — Medium
# https://leetcode.com/problems/bitwise-ors-of-subarrays/
# Submission 2198965496 — Accepted, Python3
#
# My thinking: the OR of a subarray ending here
# is just each earlier OR with the new number
# added. There are only ever a few distinct
# values — at most the number of bits — so I
# keep that small set and collect everything I
# have seen.

from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        seen = set()
        current = set()
        for num in arr:
            current = {num | prev for prev in current} | {num}
            seen |= current
        return len(seen)
