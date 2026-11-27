# 3079. Find the Sum of Encrypted Integers (Easy)
# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/
# Submission 2199973982 — Accepted, Python3
from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        # My thinking: encrypting a number means writing
        # its biggest digit in every place. I work out
        # the biggest digit and how many digits there
        # are, build that repeated-digit number, and add
        # them all up.
        total = 0
        for num in nums:
            digits = str(num)
            biggest = max(digits)
            total += int(biggest * len(digits))
        return total
