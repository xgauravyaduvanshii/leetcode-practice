# LeetCode 967. Numbers With Same Consecutive Differences — Medium
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# Submission 2198978897 — Accepted, Python3
#
# My thinking: I build the numbers digit by
# digit. From each last digit, the next digit can
# only be k higher or k lower — and when k is
# zero, those two are the same digit, so I only
# go one way.

from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []

        def build(length, num):
            if length == n:
                result.append(num)
                return
            last = num % 10
            if last + k <= 9:
                build(length + 1, num * 10 + last + k)
            if k > 0 and last - k >= 0:
                build(length + 1, num * 10 + last - k)

        for start in range(1, 10):
            build(1, start)
        return result
