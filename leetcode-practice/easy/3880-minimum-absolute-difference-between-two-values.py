# 3880. Minimum Absolute Difference Between Two Values (Easy)
# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/
# Submission 2200083972 — Accepted, Python3
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        # My thinking: the closest 1 and 2 must be
        # neighbours in the order they appear. I walk
        # the array remembering the latest 1 and the
        # latest 2, and keep the smallest gap between
        # them.
        last_one = -1
        last_two = -1
        best = None
        for i, x in enumerate(nums):
            if x == 1:
                last_one = i
                if last_two != -1:
                    gap = i - last_two
                    best = gap if best is None else min(best, gap)
            elif x == 2:
                last_two = i
                if last_one != -1:
                    gap = i - last_one
                    best = gap if best is None else min(best, gap)
        return -1 if best is None else best
