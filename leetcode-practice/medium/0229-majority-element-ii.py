# LeetCode 229. Majority Element II — Medium
# https://leetcode.com/problems/majority-element-ii/
# Submission 2198462398 — Accepted, Python3
#
# My thinking: at most two numbers can appear more
# than a third of the time, so I track two
# candidates the Boyer-Moore way — a matching
# number strengthens its candidate, a different
# one weakens both, and an empty slot takes the
# new number. The candidates are only guesses, so
# I count each one properly at the end and keep
# only those that truly pass a third.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = None
        count1 = count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        return [c for c in (cand1, cand2) if c is not None and nums.count(c) > len(nums) // 3]
