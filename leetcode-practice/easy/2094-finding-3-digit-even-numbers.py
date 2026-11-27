# LeetCode 2094. Finding 3-Digit Even Numbers — Easy
# https://leetcode.com/problems/finding-3-digit-even-numbers/
# Submission 2197612574 — Accepted, Python3
#
# My thinking: I try every ordered triple of three
# distinct digits. A triple is valid when the first
# digit is not zero and the last digit is even. I
# collect the valid numbers in a set (to drop
# duplicates) and return them sorted.

from itertools import permutations


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        result = set()
        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                result.add(a * 100 + b * 10 + c)
        return sorted(result)
