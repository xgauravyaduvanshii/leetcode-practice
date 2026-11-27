# LeetCode 1310. XOR Queries of a Subarray — Medium
# https://leetcode.com/problems/xor-queries-of-a-subarray/
# Submission 2199028378 — Accepted, Python3
#
# My thinking: a running xor lets me answer any
# range in one step — the xor up to the right
# end, xored with the xor before the left end.

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for value in arr:
            prefix.append(prefix[-1] ^ value)
        return [prefix[right + 1] ^ prefix[left] for left, right in queries]
