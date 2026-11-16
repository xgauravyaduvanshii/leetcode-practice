# LeetCode 1512. Number of Good Pairs — Easy
# https://leetcode.com/problems/number-of-good-pairs/
# Submission 2197583226 — Accepted, Python3
#
# My thinking: a good pair is two equal numbers, and
# I count pairs as I go. Each time I see a number,
# it forms a pair with every earlier copy of that
# same number — so I add the count so far, then
# bump the count.

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counts = {}
        pairs = 0
        for x in nums:
            pairs += counts.get(x, 0)
            counts[x] = counts.get(x, 0) + 1
        return pairs
