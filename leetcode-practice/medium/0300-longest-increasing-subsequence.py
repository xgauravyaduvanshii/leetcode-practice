# LeetCode 300. Longest Increasing Subsequence — Medium
# https://leetcode.com/problems/longest-increasing-subsequence/
# Submission 2198735798 — Accepted, Python3
#
# My thinking: I keep the smallest possible tail for
# an increasing run of each length. Each new number
# either extends the longest run or replaces the
# first tail that is at least as big — the number of
# tails at the end is the longest run's length.

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            index = bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num
        return len(tails)
