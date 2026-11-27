# LeetCode 2178. Maximum Split of Positive Even Integers — Medium
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/
# Submission 2204487972 — Accepted, Python3
#
# My thinking: an odd sum can never be split into even parts. For an
# even sum, taking the smallest even numbers 2, 4, 6, ... greedily gives
# the most parts, because any valid split can be reshaped to use small
# numbers first. The leftover remainder is smaller than the next even
# number, so I add it to the largest part — the sum stays right and all
# parts stay distinct.
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        if finalSum % 2 == 1:
            return []
        ans = []
        cur = 2
        total = 0
        while total + cur <= finalSum:
            ans.append(cur)
            total += cur
            cur += 2
        rem = finalSum - total
        if rem > 0:
            ans[-1] += rem
        return ans
