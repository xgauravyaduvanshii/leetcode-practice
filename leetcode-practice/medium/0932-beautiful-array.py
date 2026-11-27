# LeetCode 932. Beautiful Array — Medium
# https://leetcode.com/problems/beautiful-array/
# Submission 2198972332 — Accepted, Python3
#
# My thinking: odds and evens never make an
# arithmetic middle together — an odd plus an
# even is odd, never twice a number. So I build
# the array by keeping all the odds first, then
# the evens, growing it until it is long enough.

from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]
        while len(result) < n:
            result = [2 * x - 1 for x in result] + [2 * x for x in result]
        return [x for x in result if x <= n]
