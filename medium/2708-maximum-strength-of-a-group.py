# LeetCode 2708. Maximum Strength of a Group — Medium
# https://leetcode.com/problems/maximum-strength-of-a-group/
# Submission 2205197985 — Accepted, Python3
#
# My thinking: take every positive number, and take the
# negatives in pairs — two negatives multiply to a positive,
# so keep the largest-magnitude ones and drop the smallest
# one when the count is odd. If nothing survives, the best
# group is a single 0 when one exists, otherwise the largest
# (least negative) element on its own.
class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        pos = [x for x in nums if x > 0]
        neg = sorted((x for x in nums if x < 0), key=abs, reverse=True)
        if len(neg) % 2 == 1:
            neg.pop()
        if not pos and not neg:
            return 0 if 0 in nums else max(nums)
        ans = 1
        for x in pos + neg:
            ans *= x
        return ans
