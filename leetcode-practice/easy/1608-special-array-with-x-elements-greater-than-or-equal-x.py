# LeetCode 1608. Special Array With X Elements Greater Than or Equal X — Easy
# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
# Submission 2197589162 — Accepted, Python3
#
# My thinking: x can only be between 0 and the
# length of the array. I try each one, count how
# many numbers are at least x, and return the
# first x where that count equals x. If none
# works, the answer is -1.

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n = len(nums)
        for x in range(n + 1):
            count = 0
            for v in nums:
                if v >= x:
                    count += 1
            if count == x:
                return x
        return -1
