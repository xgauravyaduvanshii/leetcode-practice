# LeetCode 2843. Count Symmetric Integers — Easy
# https://leetcode.com/problems/count-symmetric-integers/
# Submission 2198421055 — Accepted, Python3
#
# My thinking: a symmetric integer has an even
# number of digits and the two halves add up to the
# same total. I simply check every number in the
# range, skipping any with an odd digit count, and
# count the ones whose halves match.

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            digits = str(num)
            if len(digits) % 2:
                continue
            half = len(digits) // 2
            if sum(map(int, digits[:half])) == sum(map(int, digits[half:])):
                count += 1
        return count
