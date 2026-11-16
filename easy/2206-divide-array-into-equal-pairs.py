# LeetCode 2206. Divide Array Into Equal Pairs — Easy
# https://leetcode.com/problems/divide-array-into-equal-pairs/
# Submission 2197617844 — Accepted, Python3
#
# My thinking: the array can be split into equal
# pairs exactly when every number appears an even
# number of times. I count the occurrences and check
# that none is odd.

from collections import Counter


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        return all(c % 2 == 0 for c in Counter(nums).values())
