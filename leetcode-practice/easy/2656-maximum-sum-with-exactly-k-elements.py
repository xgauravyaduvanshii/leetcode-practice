# LeetCode 2656. Maximum Sum With Exactly K Elements — Easy
# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
# Submission 2197812683 — Accepted, Python3
#
# My thinking: the best move every time is to take
# the biggest number, which then grows by 1. So I
# take the maximum and add it, then the maximum
# plus one, and so on for k steps.

from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        return sum(m + i for i in range(k))
