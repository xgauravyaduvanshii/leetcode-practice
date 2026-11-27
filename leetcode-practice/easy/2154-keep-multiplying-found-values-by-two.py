# LeetCode 2154. Keep Multiplying Found Values by Two — Easy
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/
# Submission 2197615750 — Accepted, Python3
#
# My thinking: I put the numbers in a set, then keep
# doubling the original value as long as it is in
# the set. The first value I don't find is the
# answer.

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original *= 2
        return original
