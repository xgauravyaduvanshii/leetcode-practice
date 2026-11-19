# LeetCode 1291. Sequential Digits — Medium
# https://leetcode.com/problems/sequential-digits/
# Submission 2199024075 — Accepted, Python3
#
# My thinking: there are only a handful of
# numbers whose digits run in order, so I build
# them all — every length, every starting digit
# — and keep the ones inside the range.

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for length in range(2, 10):
            for start in range(1, 11 - length):
                number = 0
                for digit in range(start, start + length):
                    number = number * 10 + digit
                if low <= number <= high:
                    result.append(number)
        return result
