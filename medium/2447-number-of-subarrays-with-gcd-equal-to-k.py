# LeetCode 2447. Number of Subarrays With GCD Equal to K — Medium
# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/
# Submission 2204949151 — Accepted, Python3
#
# My thinking: keep the distinct GCDs of all subarrays ending at
# the current position — there are only a handful, because GCDs can
# only shrink a few times. Extend each with the new element, merge
# equal GCDs, and count how many of them equal k.
import math


class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        res = 0
        prev = []
        for x in nums:
            cur = [(x, 1)]
            for g, c in prev:
                ng = math.gcd(g, x)
                if ng == cur[-1][0]:
                    cur[-1] = (ng, cur[-1][1] + c)
                else:
                    cur.append((ng, c))
            prev = cur
            for g, c in cur:
                if g == k:
                    res += c
        return res
