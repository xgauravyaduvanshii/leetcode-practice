# LeetCode 2529. Maximum Count of Positive Integer and Negative Integer — Easy
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
# Submission 2197799285 — Accepted, Python3
#
# My thinking: I count the positives and the
# negatives separately — zeros count for neither —
# and the answer is the bigger of the two counts.

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos = sum(1 for x in nums if x > 0)
        neg = sum(1 for x in nums if x < 0)
        return max(pos, neg)
