# LeetCode 179. Largest Number — Medium
# https://leetcode.com/problems/largest-number/
# Submission 2198438804 — Accepted, Python3
#
# My thinking: two numbers should be ordered by
# which way round they read bigger when joined —
# "9" goes before "34" because "934" beats "349".
# I sort all the numbers as strings by that rule
# and join them. If the result starts with a zero,
# every number was zero and the answer is just "0".

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        words = [str(n) for n in nums]
        words.sort(key=cmp_to_key(compare))
        result = "".join(words)
        return "0" if result[0] == "0" else result
