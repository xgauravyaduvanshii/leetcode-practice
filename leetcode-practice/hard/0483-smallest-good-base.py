# LeetCode 483. Smallest Good Base — Hard
# https://leetcode.com/problems/smallest-good-base/
# Submission 2198660615 — Accepted, Python3
#
# My thinking: a good base means n is all ones in that
# base. I try the longest length first — the smallest
# base comes from the longest string of ones — and for
# each length I binary search the base, building the
# value 1 + k + k^2 + ... and stopping early once it
# passes n.

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        value = int(n)
        for length in range(62, 1, -1):
            low, high = 2, 10 ** 18
            while low <= high:
                base = (low + high) // 2
                total = 1
                power = 1
                for _ in range(length - 1):
                    power *= base
                    total += power
                    if total > value:
                        break
                if total == value:
                    return str(base)
                if total > value:
                    high = base - 1
                else:
                    low = base + 1
        return str(value - 1)
