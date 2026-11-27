# LeetCode 2256. Minimum Average Difference — Medium
# https://leetcode.com/problems/minimum-average-difference/
# Submission 2204518139 — Accepted, Python3
#
# My thinking: I sweep the split point from left to right, keeping the
# running sum of the left part so both averages come from one pass. The
# left average is the left sum over its length and the right average is
# the remaining sum over its length (zero when nothing remains). I keep
# the first index with the smallest absolute difference.
class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        best_idx = 0
        best_diff = float('inf')
        for i, x in enumerate(nums):
            left_sum += x
            left_avg = left_sum // (i + 1)
            right_count = n - i - 1
            right_avg = (total - left_sum) // right_count if right_count > 0 else 0
            diff = abs(left_avg - right_avg)
            if diff < best_diff:
                best_diff = diff
                best_idx = i
        return best_idx
