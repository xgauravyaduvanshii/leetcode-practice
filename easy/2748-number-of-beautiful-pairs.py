# LeetCode 2748. Number of Beautiful Pairs — Easy
# https://leetcode.com/problems/number-of-beautiful-pairs/
# Submission 2198358663 — Accepted, Python3
#
# My thinking: a pair is beautiful when the first
# digit of the earlier number and the last digit
# of the later number share no common factor
# except 1. I check every pair that way — the
# list is short enough that trying them all works.

from math import gcd
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(len(nums)):
            first_digit = int(str(nums[i])[0])
            for j in range(i + 1, len(nums)):
                last_digit = nums[j] % 10
                if gcd(first_digit, last_digit) == 1:
                    pairs += 1
        return pairs
