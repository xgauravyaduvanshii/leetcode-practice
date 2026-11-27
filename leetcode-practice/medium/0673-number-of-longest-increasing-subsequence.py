# LeetCode 673. Number of Longest Increasing Subsequence — Medium
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# Submission 2198907961 — Accepted, Python3
#
# My thinking: for each number I track the length
# of the longest increasing subsequence ending
# there, and how many such subsequences there are.
# Extending a shorter one starts a new count;
# extending an equal one adds to it.

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengths = [1] * n
        counts = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        longest = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == longest)
