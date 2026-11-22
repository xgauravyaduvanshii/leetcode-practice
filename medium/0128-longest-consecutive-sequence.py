# LeetCode 128. Longest Consecutive Sequence — Medium
# https://leetcode.com/problems/longest-consecutive-sequence/
# Submission 2200894797 — Accepted, Python3
#
# My thinking: a run can only start at a number whose
# predecessor is missing, so I put everything in a set
# and walk forward only from those starts.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        best = 0
        for num in seen:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                best = max(best, length)
        return best
