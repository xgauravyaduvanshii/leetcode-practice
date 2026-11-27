# LeetCode 1362. Closest Divisors — Medium
# https://leetcode.com/problems/closest-divisors/
# Submission 2199041183 — Accepted, Python3
#
# My thinking: num + 1 and num + 2 both need
# splitting, and the closer pair wins. For each
# I take the largest divisor at or below the
# square root — that pair is the closest one.

from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def divisors(n):
            for d in range(int(n ** 0.5), 0, -1):
                if n % d == 0:
                    return [d, n // d]
            return [1, n]

        first = divisors(num + 1)
        second = divisors(num + 2)
        return first if abs(first[0] - first[1]) < abs(second[0] - second[1]) else second
