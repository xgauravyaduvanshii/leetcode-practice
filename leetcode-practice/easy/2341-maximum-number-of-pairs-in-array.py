# LeetCode 2341. Maximum Number of Pairs in Array — Easy
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/
# Submission 2197623816 — Accepted, Python3
#
# My thinking: I count how many times each number
# appears. Every two copies make one pair, and the
# odd one out of each number is left over.

from collections import Counter


class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        pairs = sum(c // 2 for c in counts.values())
        leftover = sum(c % 2 for c in counts.values())
        return [pairs, leftover]
