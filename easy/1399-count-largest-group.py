# LeetCode 1399. Count Largest Group — Easy
# https://leetcode.com/problems/count-largest-group/
# Submission 2197576044 — Accepted, Python3
#
# My thinking: I group the numbers from 1 to n by
# their digit sum, count how big each group is,
# find the biggest group size, and then count how
# many groups are that big.

from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(x):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total

        counts = Counter(digit_sum(i) for i in range(1, n + 1))
        largest = max(counts.values())
        return sum(1 for v in counts.values() if v == largest)
